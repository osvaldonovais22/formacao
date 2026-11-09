"""Lista os arquivos de uma pasta do maior para o menor, com tamanho em MB.

Uso: python3 tamanhos.py <pasta> [quantidade]
Exemplos: python3 tamanhos.py ~/Downloads
          python3 tamanhos.py ~/Downloads 5
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
    if len(sys.argv) not in (2, 3):
        print("Uso: python3 tamanhos.py <pasta> [quantidade]")
        sys.exit(1)

    quantidade = 10
    if len(sys.argv) == 3:
        try:
            quantidade = int(sys.argv[2])
        except ValueError:
            quantidade = 0
        if quantidade < 1:
            print("Erro: a quantidade deve ser um número inteiro maior que zero.")
            sys.exit(1)

    pasta = os.path.expanduser(sys.argv[1])
    if not os.path.isdir(pasta):
        print(f"Erro: '{pasta}' não é uma pasta válida.")
        sys.exit(1)

    arquivos = listar_tamanhos(pasta)
    if not arquivos:
        print("Nenhum arquivo encontrado.")
        return

    total = sum(t for t, _ in arquivos)

    print(f"{min(quantidade, len(arquivos))} maiores arquivos de '{pasta}':")
    for tamanho, caminho in arquivos[:quantidade]:
        print(f"{tamanho / MB:10.2f} MB  {caminho}")

    print(f"\nTotal: {len(arquivos)} arquivo(s), {total / MB:.2f} MB")


if __name__ == "__main__":
    main()
