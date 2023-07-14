def reajusteSalario(salario, percentual):
    percentual = (float(percentual) / 100) + 1
    novoSalario = salario * percentual
    return novoSalario

salario = 1000
percentual = 15

print(reajusteSalario(salario, percentual))