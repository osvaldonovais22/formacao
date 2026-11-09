"""Lista os arquivos de uma pasta do maior para o menor, com tamanho em MB.

Uso: python3 tamanhos.py <pasta>
Exemplo: python3 tamanhos.py ~/Downloads
"""

import os
import sys

MB = 1024 * 1024


def listar_tamanhos(pasta):
    arquivos = []
    for raiz, _, nomes in os.walk(pasta):
        for nome in nomes:
            caminho = os.path.join(raiz, nome)
            if os.path.islink(caminho):
                continue  # ignora atalhos para não contar duas vezes
            try:
                tamanho = os.path.getsize(caminho)
            except OSError:
                continue  # arquivo inacessível ou removido durante a leitura
            arquivos.append((tamanho, caminho))

    arquivos.sort(reverse=True)
    return arquivos


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 tamanhos.py <pasta>")
        sys.exit(1)

    pasta = os.path.expanduser(sys.argv[1])
    if not os.path.isdir(pasta):
        print(f"Erro: '{pasta}' não é uma pasta válida.")
        sys.exit(1)

    arquivos = listar_tamanhos(pasta)
    if not arquivos:
        print("Nenhum arquivo encontrado.")
        return

    for tamanho, caminho in arquivos:
        print(f"{tamanho / MB:10.2f} MB  {caminho}")

    total = sum(t for t, _ in arquivos)
    print(f"\n{len(arquivos)} arquivo(s), total: {total / MB:.2f} MB")


if __name__ == "__main__":
    main()
