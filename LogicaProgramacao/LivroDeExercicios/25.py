def transacoes (saldo, credito, debito):
    resultado = saldo - debito + credito
    return resultado

conta = 748596
saldo = 150

novoSaldo = transacoes(saldo, 0, 200)

saldo = novoSaldo

if saldo < 0:
    print("Seu saldo está NEGATIVO: R$ ", saldo)
else:
    print("Seu saldo é: R$ ", saldo)
