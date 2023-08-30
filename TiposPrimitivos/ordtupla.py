def buscaMenor(arr):
    menor = arr[0][1]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i][1] < menor:
            menor = arr[i][1]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoporSelecao([(2,5), (1,2), (4,4), (2,3), (2,1)]))


