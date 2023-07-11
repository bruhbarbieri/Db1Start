from cs50 import get_float

def areaRetangulo(base, altura):
    area = base * altura
    return area

base = get_float("Digite o valor da base do retangulo: ")
altura = get_float("Digite o valor da altura do retangulo: ")

print("A aréa do retangulo é: ", areaRetangulo(base, altura))
