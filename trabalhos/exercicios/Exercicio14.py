# Exercício 14: Verificação de Vogal ou Consoante
# Solicite ao usuário para digitar uma letra e determine se é uma vogal ou uma consoante.

letra = str(input("Digite uma letra: ")).lower()

if letra in 'aeiou':
    print("Vogal!")

else:
    print("Consoante!")
