class String:
    listString = []

    def adicionarString(string):
        __class__.listString.append(string)

    def inverterString():
        for str in __class__.listString[::-1]:
            print(str)

String.adicionarString("bruna")
String.adicionarString("mariana")
String.adicionarString("giovane")
String.adicionarString("olivia")

String.inverterString()