from cs50 import get_int

def idadeDias (ano, mes, dia):
    ano = ano * 365
    mes = mes * 30
    total = ano + mes + dia
    return total

print("digite a sua idade em anos, meses e dias")

ano = get_int("Anos: ")
mes = get_int("Meses: ")
dia = get_int("Dias: ")

print("A sua idade em dias é: ", idadeDias(ano, mes, dia), "dias")
