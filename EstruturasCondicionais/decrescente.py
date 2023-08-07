n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")
n3 = input("Digite o terceiro número: ")

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)

if (n1 > n2 and n1 < n3) or (n1 < n2 and n1 > n3):
    print(n1)
elif (n2 > n1 and n2 < n3) or (n2 < n1 and n2 > n3) :
    print(n2)
else:
    print(n3)

if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n1 and n2 < n3:
    print(n2)
else:
    print(n3)