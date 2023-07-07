from cs50 import get_int


def fat(n):
    total = 1
    for i in range(n):
        total = total * (i+1)
    return total

fatorial= get_int("Qual número deseja saber seu fatorial? ")

print("o fatorial de", fatorial, "é: ", fat(fatorial) )