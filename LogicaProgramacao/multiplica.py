from cs50 import get_int

def multiplicacao(numero, multiplicador):
    resultado = 0
    for i in range(multiplicador):
        resultado = resultado + numero
    print ("O resultado da multiplicação é: ", resultado)

numero = get_int("Digite o numero: ")
multiplicador = get_int("Digite o multiplicador: ")

multiplicacao(numero, multiplicador)
