# Variável
peso = 80
altura = 1.75
imc = peso / altura ** 2
print(round(imc, 1))

# Condição (if)
if imc >= 25:
    print("Sobrepeso")
else:
    print("Normal")

# Repetição (for)
for numero in range(1, 11):
    print(numero)

# Exercício final: as três juntas
pesos = [50, 70, 85, 100]
for peso in pesos:
    imc = peso / altura ** 2
    if imc >= 30:
        print(peso, round(imc, 1), "Obesidade")
    elif imc >= 25:
        print(peso, round(imc, 1), "Sobrepeso")
    elif imc >= 18.5:
        print(peso, round(imc, 1), "Normal")
    else:
        print(peso, round(imc, 1), "Baixo peso")
        