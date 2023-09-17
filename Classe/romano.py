class Romano:
    def __init__(self, number):
        self.number = number

    def transf(self):
        numero = self.number
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ''
        i = 0
        while numero > 0:
            count = numero // val[i]
            if count > 0:
                roman = roman + (syms[i] * count)
                numero = numero - (val[i] * count)
            i += 1
        return roman

romano = Romano(19)

print (romano.transf())



