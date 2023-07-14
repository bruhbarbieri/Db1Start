def percentualVotos(branco, nulos, validos, totalEleitores):
    percentualBranco = (float(branco) * 100) / totalEleitores
    percentualNulos = (float(nulos) * 100) / totalEleitores
    percentualValidos = (float(validos) * 100) / totalEleitores
    return print("Percentual de Votos Brancos:", percentualBranco, "%  "
                 "Percentual de Votos Nulos:", percentualNulos, "%  "
                 "Percentual de Votos Validos:", percentualValidos, "%  ")

branco = float(50545)
nulos = float(40122)
validos = float(155325)
totalEleitores = float(357487)

percentualVotos(branco, nulos, validos, totalEleitores)
