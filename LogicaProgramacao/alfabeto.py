from cs50 import get_string

def busca(lista, item):
    for i in range (len(lista)):
        if item == lista[i]:
            return print("a posição da letra é: ", i + 1)


alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "X", "Z"]

letra = get_string("Digite a letra que deseja encontrar: ")

busca(alfabeto, letra)