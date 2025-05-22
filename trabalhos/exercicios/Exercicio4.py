# Exercício 4: Cálculo de IMC
# Peça ao usuário seu peso (em kg) e altura (em metros), e calcule o Índice de Massa Corporal (IMC)
# utilizando a fórmula: IMC = peso / (altura * altura).

peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

imc = peso / (altura ** 2)

print(f"Seu IMC é de {imc:.2f}")
