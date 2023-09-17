class Romano2:
    def __init__(self, roman):
        self.roman = roman

    def transf(self):
        romano = self.roman
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev_value = 0

        for char in romano[::-1]:
            value = roman_dict[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
            
        return result

romano = Romano2("XIX")

print (romano.transf())