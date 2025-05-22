# Exercício 5: Cálculo de Desconto
# Peça ao usuário o valor de um produto e o percentual de desconto. 
# Calcule e mostre o valor com o desconto aplicado.

valor = float(input("Digite o valor do produto: R$ "))
desconto = float(input("Digite o percentual de desconto: (%) "))

descontado = valor - (valor * desconto / 100)

print(f"O preço final do produto é de R${descontado:.2f}")