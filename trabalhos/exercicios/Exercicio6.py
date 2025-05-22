# Exercício 6: Calculadora de Juros Simples
# Solicite ao usuário um valor principal, a taxa de juros (em porcentagem) e o número de anos. Calcule o
# montante final utilizando a fórmula: Montante = principal + (principal * taxa de juros * anos / 100).

valor = float(input("Digite o valor principal: "))
taxa = float(input("Digite o valor da taxa de juros: "))
anos = int(input("Digite o número de anos: "))

montante = valor + (valor * taxa * anos / 100)

print(f"Montante final após {anos} anos é de R${montante}.")


