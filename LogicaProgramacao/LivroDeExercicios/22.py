from cs50 import get_float

def remuneracaoFinal(horasTrab, salarioHora):
    horaExtra = horasTrab - 160
    salarioExtra = salarioHora * 1.5
    if horasTrab < 160:
        print("Houve faltas não justificadas este mês")
        remuneracaoFinal = (horasTrab * salarioHora)
        return print("Sua remuneração final neste mês é de R$", remuneracaoFinal)
    else:
        remuneracaoFinal = (160 * salarioHora) + (horaExtra * salarioExtra)
        return print("Sua remuneração final neste mês é de R$", remuneracaoFinal)

horas = get_float("Horas Trabalhadas: ")
salario = get_float("Salario por hora: ")

remuneracaoFinal(horas, salario)
