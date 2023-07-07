from cs50 import get_float

def media(valores, quantidadeValores):
    n = valores / quantidadeValores
    print("Média das notas:", n)
    if n >= 6:
        return print("Você está aprovado")
    else:
        return print("Você está reprovado")

notas = get_float("Informe a nota: ") #Quando quiser parar de informar as notas, digite 0
soma = 0
quantidadeNotas = 0

while notas != 0:
    quantidadeNotas = quantidadeNotas + 1
    soma = soma + notas
    print("Total: ", soma)
    notas = get_float("Informe a nota: ") #Quando quiser parar de informar as notas, digite 0

print ("Resultado da Soma: ", soma)

media(soma, quantidadeNotas)