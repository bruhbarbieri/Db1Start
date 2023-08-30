transposta = []
matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

for i in range(len(matriz[0])):
    linha_transposta = []
    for linha in matriz:
        linha_transposta.append(linha[i])
    transposta.append(linha_transposta)

print(transposta)