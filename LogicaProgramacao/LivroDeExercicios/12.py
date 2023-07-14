def transformaCelsius (tempF):
    tempC = ((float(tempF) - 32) / 9) * 5
    return tempC

print("Temperatura Graus Celsius:", transformaCelsius(212), "°")