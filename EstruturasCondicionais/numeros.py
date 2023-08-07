n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")
n3 = input("Digite o terceiro número: ")

if n1 > n2 and n1 > n3:
    print(n1, "é o maior número")
elif n2 > n1 and n2 > n3:
    print(n2, "é o maior número")
else:
    print(n3, "é o maior número")

if n1 < n2 and n1 < n3:
    print(n1, "é o menor número")
elif n2 < n1 and n2 < n3:
    print(n2, "é o menor número")
else:
    print(n3, "é o menor número")