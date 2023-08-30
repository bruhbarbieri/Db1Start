palavra = "desenvolvedor"
verificadas = []
total = {}

for letra in palavra:
    if letra in verificadas:
        continue
    else:
        contagem = palavra.count(letra)
        total[letra] = contagem
        verificadas.append(letra)

print(total)