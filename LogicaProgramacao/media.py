from cs50 import get_float
from cs50 import get_int

notas = []
quantidadeNotas = get_int("quantas notas deseja acrescentar? ")

for i in range(quantidadeNotas):
    notas.append(get_float("Informe a próxima nota: "))

def media():
    n = sum(notas) / len(notas)
    print("Média das notas:", n)
    if n >= 6:
        return print("Você está aprovado")
    else:
        return print("Você está reprovado")

media()