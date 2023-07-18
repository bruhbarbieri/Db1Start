while True:
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Entrada Inválida!! Digite de forma numérica!")
    else:
        print("O numero informado é:", numero)
        break