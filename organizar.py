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

Uso: python3 organizar.py <pasta>
Exemplo: python3 organizar.py ~/Downloads
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


def destino_sem_conflito(pasta_destino, nome):
    caminho = os.path.join(pasta_destino, nome)
    base, extensao = os.path.splitext(nome)
    contador = 1
    while os.path.exists(caminho):
        caminho = os.path.join(pasta_destino, f"{base} ({contador}){extensao}")
        contador += 1
    return caminho


def organizar(pasta):
    contagem = Counter()
    for nome in os.listdir(pasta):
        origem = os.path.join(pasta, nome)
        if not os.path.isfile(origem) or os.path.islink(origem):
            continue  # pula subpastas e atalhos

        categoria = categoria_do(nome)
        pasta_destino = os.path.join(pasta, categoria)
        os.makedirs(pasta_destino, exist_ok=True)

        destino = destino_sem_conflito(pasta_destino, nome)
        shutil.move(origem, destino)
        print(f"{nome} -> {os.path.relpath(destino, pasta)}")
        contagem[categoria] += 1

    print("\nResumo por pasta:")
    for categoria in [*CATEGORIAS, OUTROS]:
        if contagem[categoria]:
            print(f"  {categoria}: {contagem[categoria]}")
    print(f"\n{sum(contagem.values())} arquivo(s) organizado(s).")


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 organizar.py <pasta>")
        sys.exit(1)

    pasta = os.path.expanduser(sys.argv[1])
    if not os.path.isdir(pasta):
        print(f"Erro: '{pasta}' não é uma pasta válida.")
        sys.exit(1)

    organizar(pasta)


if __name__ == "__main__":
    main()
