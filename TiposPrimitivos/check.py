dicionario = {}
retorno = "sim"

while retorno == "sim":
    chave = input("Digite a chave: ")
    dicionario[chave] = input("Digite o valor: ")
    retorno = input("Deseja adicionais mais itens? ") #sim ou nao

chave = input("Digite a chave da pesquisa: ")

if chave in dicionario:
    print("Chave encontrada: ", dicionario[chave])
else:
    print("Chave não encontrada!!")
