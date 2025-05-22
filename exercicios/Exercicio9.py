# Exercício 9: Verificação de Idade para Dirigir
# Peça a idade do usuário e verifique se ele tem idade suficiente para dirigir (idade mínima de 18 anos).

idade = int(input("Qual a sua idade? "))

if idade < 18:
    print("Você ainda não tem idade o suficiente para dirigir.")

else:
    print("Você já tem idade o suficiente para dirigir.")

