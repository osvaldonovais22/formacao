import math

MENSAGEM_ERRO = "Valor inválido, digite só números"
MENSAGEM_ZERO_NEGATIVO = "Valor inválido, digite um número maior que zero"


def ler_numero(pergunta):
    try:
        valor = float(input(pergunta).replace(",", "."))
    except ValueError:
        print(MENSAGEM_ERRO)
        raise SystemExit
    if not math.isfinite(valor):
        print(MENSAGEM_ERRO)
        raise SystemExit
    if valor <= 0:
        print(MENSAGEM_ZERO_NEGATIVO)
        raise SystemExit
    return valor


peso = ler_numero("Peso (kg): ")
altura = ler_numero("Altura (m): ")

imc = peso / altura ** 2

if imc < 18.5:
    classificacao = "Baixo peso"
elif imc < 25:
    classificacao = "Normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"IMC {imc:.1f} - {classificacao}")
