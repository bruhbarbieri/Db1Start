palavras = ["acb", "xyz", "aba", "1221"]
achados = []

for palavra in palavras:
    if len(palavra) > 2 and palavra[0] == palavra[-1]:
        achados.append(palavra)
    else:
        continue

print(len(achados))


