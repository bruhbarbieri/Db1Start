def remuneracaoFinal (carrosVendidos, totalVendas, salario, bonusCarro):
    totalBonus = float(bonusCarro) * float(carrosVendidos)
    comissao = float(totalVendas) * 0.05
    remuneracaoFinal = salario + totalBonus + comissao
    return remuneracaoFinal

print("A remuneração final do vendedor é de: R$", remuneracaoFinal(2, 197000, 3000, 500))