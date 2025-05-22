# Exercício 1: Preço a pagar
# Crie um programa que pergunte ao usuário o valor do café (um número)
# e pergunte para ele quantos cafés ele irá querer comprar e apresente o resultado a pagar.

preco_cafe = 1.50

print("=-"*20)
escolha = int(input("Olá, quantos cafés você deseja hoje? "))
print("--------- Valor ---------")
print("Café normal: R$1,50")

valor_total = preco_cafe * escolha

print(f"Você vai querer {escolha}, o valor total é de R${valor_total:.2f}")






