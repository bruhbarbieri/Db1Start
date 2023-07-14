from cs50 import get_int

def consultaVoto(ano):
    anoHoje = 2026
    idade = anoHoje - ano
    if idade < 16:
        return print("Não habilitado para votação")
    else:
        return print("Habilitado para votação")

ano = get_int("Digite o ano que você nasceu: ")

consultaVoto(ano)