from cs50 import get_int

numero = get_int("Digite o número: ")

if numero < 0:
    print("NEGATIVO")
else:
    print("POSITIVO")