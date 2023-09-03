def inverso(palavra):
    novaPalavra = ""
    for letra in palavra:
        novaPalavra = letra + novaPalavra
    return novaPalavra

print(inverso("giovane"))
