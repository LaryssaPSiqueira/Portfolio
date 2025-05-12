# Dicionário com os preços das pizzas, tamanhos e refrigerantes
preco_pizza = {
    1: 10.00,  # Calabresa
    2: 15.00,  # Frango
    3: 20.00,  # Catupiry
    4: 12.00,  # Mussarela
    5: 14.00,  # Margherita
    6: 18.00,  # Bacon
    7: 16.00   # Portuguesa
}

preco_refrigerante = {
    1: 7.00,   # Coca-Cola
    2: 6.00,   # Guaraná
    3: 5.00,   # Fanta
    4: 6.50,   # Guaraná Antarctica
    5: 6.00,   # Sprite
    6: 7.50    # Coca-Cola Diet
}

preco_tamanho = {  
   'P': 10.00,  #Pequena
   'M': 15.00,  #Média
   'G': 20.00   #Grande
}

tamanho_pizza = {"P": "Pequena", "M": "Média", "G": "Grande"}

# Introdução
print("PIZZARIA COMA BASTANTE - SEJA BEM VINDO!")
print("______Cardápio - Preços_______")
print("1 - Calabresa")
print("2 - Frango")
print("3 - Catupiry")
print("4 - Mussarela")
print("5 - Margherita")
print("6 - Bacon")
print("7 - Portuguesa")

print("______Tamanho - Preços_______")
print("Pizza Pequena R$10,00")
print("Pizza Média R$15,00")
print("Pizza Grande R$20,00")

print("______Refrigerantes - Preços_______")
print("1 - Coca-Cola R$7,00")
print("2 - Guaraná R$6,00")
print("3 - Fanta R$5,00")
print("4 - Guaraná Antarctica R$6,50")
print("5 - Sprite R$6,00")
print("6 - Coca-Cola Diet R$7,50")

# Escolha do sabor da pizza
pedidopizza = int(input("Qual sabor de pizza você deseja (1 a 7)? "))
while pedidopizza not in preco_pizza:
    pedidopizza = int(input("Opção inválida. Escolha novamente o sabor (1 a 7): "))

# Escolha do tamanho da pizza
print("Digite o tamanho da pizza (P - Pequena, M - Média, G - Grande):")
tampizza = input().upper()
while tampizza not in tamanho_pizza:
    tampizza = input("Tamanho inválido. Escolha novamente (P, M, G): ").upper()

# Escolha do refrigerante
print("Faça o seu pedido para refrigerante:")
print("1 - Coca-Cola")
print("2 - Guaraná")
print("3 - Fanta")
print("4 - Guaraná Antarctica")
print("5 - Sprite")
print("6 - Coca-Cola Diet")
pedidorefri = int(input("Qual refrigerante você vai querer beber? "))
while pedidorefri not in preco_refrigerante:
    pedidorefri = int(input("Opção inválida. Escolha novamente o refrigerante (1 a 6): "))

# Calcular preço total
preco_pizza_escolhida = preco_pizza[pedidopizza]
preco_refrigerante_escolhido = preco_refrigerante[pedidorefri]
preco_tamanho_escolhido = preco_tamanho[tampizza]

# Descrição do pedido
sabor_pizza = ["Calabresa", "Frango", "Catupiry", "Mussarela", "Margherita", "Bacon", "Portuguesa"][pedidopizza - 1]
tamanho_pizza_escolhido = tamanho_pizza[tampizza]
refrigerante_escolhido = ["Coca-Cola", "Guaraná", "Fanta", "Guaraná Antarctica", "Sprite", "Coca-Cola Diet"][pedidorefri - 1]

# Preço total
precopagar = preco_pizza_escolhida + preco_refrigerante_escolhido + preco_tamanho_escolhido
pedidos = f"{sabor_pizza}, {tamanho_pizza_escolhido}, {refrigerante_escolhido}"

# Exibe o resumo do pedido e o preço total
print("_____________________________________________")
print(f"O total a pagar é: R${precopagar:.2f}")
print("_____________________________________________")
print(f"Os pedidos foram {pedidos}")
print("_____________________________________________")
print("Bom apetite e seja bem-vindo!")
