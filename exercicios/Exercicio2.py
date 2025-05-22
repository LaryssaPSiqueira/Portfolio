# Exercício 2: Conversão de Temperatura
#Peça uma temperatura em Celsius ao usuário e converta-a para Fahrenheit utilizando a fórmula:
#Fahrenheit = (Celsius * 9/5) + 32.

celsius = float(input("Digite uma temperatura em celsius para ser convertido em fahrenheit: "))

fahrenheit = (celsius * 9/5) + 32

print("=-"*40)
print(f"A temperatura convertida em fahrenheit é de {fahrenheit}")
