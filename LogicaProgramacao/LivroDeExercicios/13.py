from cs50 import get_float

def mediaFinal (n1, n2, n3):
    mediaFinal = (n1 * 2 + n2 * 3 + n3 * 5) / 10
    return mediaFinal

n1 = get_float("Digite a nota 1: ")
n2 = get_float("Digite a nota 2: ")
n3 = get_float("Digite a nota 3: ")

print("Média final:", mediaFinal(n1, n2, n3))