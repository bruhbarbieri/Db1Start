class Triangulo:
    def __init__(self, ang1, ang2, ang3):
        self.ang1 = ang1
        self.ang2 = ang2
        self.ang3 = ang3

    def checkAngulo(self):
        soma = self.ang1 + self.ang2 + self.ang3
        if soma == 180:
            print("True")
        else:
            print("False")

triangulo = Triangulo(45, 45, 90)

triangulo.checkAngulo()