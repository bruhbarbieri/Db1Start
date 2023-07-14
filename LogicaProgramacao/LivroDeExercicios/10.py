def precoFinal (percentualDistribuidor, percentualImpostos, custoFabrica):
    distribuidor = float(custoFabrica) * (float(percentualDistribuidor) / 100)
    impostos = float(custoFabrica) * (float(percentualImpostos) / 100)
    precoFinal = custoFabrica + distribuidor + impostos
    return precoFinal

print("O custo final do automovel é de: R$", precoFinal(28, 45, 1730))
