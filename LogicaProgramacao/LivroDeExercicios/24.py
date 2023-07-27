salario = 1500
vendas = 2000

if vendas <= 1500:
    comissao = vendas * 0.03
    total = salario + comissao
    print("A remunureção total é: R$", total)
else:
    vendas = vendas - 1500
    comissao = (vendas * 0.05) + 45
    total = salario + comissao
    print("A remunureção total é: R$", total)