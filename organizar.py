"""Organiza os arquivos de uma pasta em subpastas por tipo.

Tipos:
    Imagens    -> jpg, jpeg, png
    PDFs       -> pdf
    Vídeos     -> mp4
    Documentos -> docx, xlsx
    STL        -> stl
    Outros     -> qualquer outra extensão (ou sem extensão)

Só os arquivos que estão diretamente na pasta são movidos; as subpastas
já existentes são deixadas como estão. Se já existir um arquivo com o
mesmo nome no destino, o novo recebe um sufixo (ex.: foto (1).jpg).

Uso: python3 organizar.py <pasta> [--teste]
Exemplo: python3 organizar.py ~/Downloads
Com --teste: só mostra o que seria feito, sem mover nada.
"""

import os
import shutil
import sys
from collections import Counter

CATEGORIAS = {
    "Imagens": {"jpg", "jpeg", "png"},
    "PDFs": {"pdf"},
    "Vídeos": {"mp4"},
    "Documentos": {"docx", "xlsx"},
    "STL": {"stl"},
}
OUTROS = "Outros"


def categoria_do(nome):
    extensao = os.path.splitext(nome)[1][1:].lower()  # "foto.JPG" -> "jpg"
    for pasta, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return pasta
    return OUTROS


def destino_sem_conflito(pasta_destino, nome, reservados=frozenset()):
    # "reservados": caminhos que já foram escolhidos nesta execução
    # (usado no modo --teste, quando nada é movido de verdade).
    caminho = os.path.join(pasta_destino, nome)
    base, extensao = os.path.splitext(nome)
    contador = 1
    while os.path.exists(caminho) or caminho in reservados:
        caminho = os.path.join(pasta_destino, f"{base} ({contador}){extensao}")
        contador += 1
    return caminho


def organizar(pasta, teste=False):
    contagem = Counter()
    reservados = set()
    if teste:
        print("MODO TESTE: nada será movido, só mostrando o que seria feito.\n")
    for nome in os.listdir(pasta):
        origem = os.path.join(pasta, nome)
        if not os.path.isfile(origem) or os.path.islink(origem):
            continue  # pula subpastas e atalhos

        categoria = categoria_do(nome)
        pasta_destino = os.path.join(pasta, categoria)

        if teste:
            destino = destino_sem_conflito(pasta_destino, nome, reservados)
            reservados.add(destino)
        else:
            os.makedirs(pasta_destino, exist_ok=True)
            destino = destino_sem_conflito(pasta_destino, nome)
            shutil.move(origem, destino)

        print(f"{nome} -> {os.path.relpath(destino, pasta)}")
        contagem[categoria] += 1

    print("\nResumo por pasta:")
    for categoria in [*CATEGORIAS, OUTROS]:
        if contagem[categoria]:
            print(f"  {categoria}: {contagem[categoria]}")
    if teste:
        print(f"\n{sum(contagem.values())} arquivo(s) seriam organizado(s). Nada foi movido.")
    else:
        print(f"\n{sum(contagem.values())} arquivo(s) organizado(s).")


def main():
    args = sys.argv[1:]
    teste = "--teste" in args
    args = [a for a in args if a != "--teste"]

    if len(args) != 1:
        print("Uso: python3 organizar.py <pasta> [--teste]")
        sys.exit(1)

    pasta = os.path.expanduser(args[0])
    if not os.path.isdir(pasta):
        print(f"Erro: '{pasta}' não é uma pasta válida.")
        sys.exit(1)

    organizar(pasta, teste=teste)


if __name__ == "__main__":
    main()
