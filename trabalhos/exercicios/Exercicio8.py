# Exercício 8: Numeros negativos
# Crie um programa utilizando um vetor de 4 posições onde o usuário irá digitar 4 números.
# O programa irá retornar quantos números negativos foram digitados.


neg = 0

for i in range(4):
    num = int(input(f"Digite o {i + 1} número: "))

    if num < 0:
        neg +=1


print(f"Você digitou {neg} números negativos.")