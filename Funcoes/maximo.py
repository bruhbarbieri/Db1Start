def maiorNumero(lista):
    maior = 0
    for item in lista:
        if item > maior:
            maior = item
        else:
            pass
    return maior

print("Maior número:", maiorNumero([1, 6, 5, 4]))
