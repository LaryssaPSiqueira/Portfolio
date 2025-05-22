# Exercício 7: Troca de Valores
# Solicite ao usuário dois valores e troque o valor da primeira variável com o da segunda variável, e vice- versa.

a = input("Digite o valor da primeira variável: ")
b = input("Digite o valor da segunda variável: ")

a, b = b, a

print(f"Agora a primeira variável vale {a} e a segunda vale: {b}.")
