# Exercício 16: Classificação de Idade
# Solicite a idade do usuário e classifique-a em "Criança", "Adolescente", "Adulto Jovem" ou "Adulto".

idade = int(input("Digite a sua idade: "))

if idade <= 10:
    print("Criança!")

elif idade <= 14:
    print("Adolescente!")

elif idade <= 18:
    print("Adulto Jovem!")

else:
    print("Adulto!")
