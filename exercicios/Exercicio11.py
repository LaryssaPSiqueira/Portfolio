# Exercício 11: Classificação de Triângulos
# Peça ao usuário os comprimentos dos três lados de um triângulo e determine se é equilátero, isósceles ou escaleno.

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))


if a == b == c:
        print("Triângulo equilátero.")

elif a == b or a == c or b == c:
        print("Triângulo isósceles.")
    
else:
        print("Triângulo escaleno.")
