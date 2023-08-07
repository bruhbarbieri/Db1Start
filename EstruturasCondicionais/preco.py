preco1 = float(input("Digite o primeiro preço: "))
preco2 = float(input("Digite o segundo preço: "))
preco3 = float(input("Digite o terceiro preço: "))

if preco1 < preco2 and preco1 < preco3:
    print("O primeiro é o mais barato:", preco1)
elif preco2 < preco1 and preco2 < preco3:
    print("O segundo é o mais barato:", preco2)
else:
    print("O terceiro é o mais barato:", preco3)