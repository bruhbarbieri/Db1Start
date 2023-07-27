from cs50 import get_int

valor = get_int("Digite um número: ")

if valor == 0:
    print("Seu número é ZERO")
elif valor > 0:
    print("Seu número é POSITIVO")
else:
    print("Seu número é NEGATIVO")
