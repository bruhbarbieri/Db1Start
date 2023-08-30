result = []
entradas = [1, 20, 13, 5, 21, 16]


for numero in entradas:
    if numero < 10:
        result.append((numero - 1, numero, numero + 1))
    elif numero % 2 == 0:
        result.insert(0, (numero, numero + 2, numero * 2))
    else:
        result.append(numero)

print(result)