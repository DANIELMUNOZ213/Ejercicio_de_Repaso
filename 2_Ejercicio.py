def calcular_area_circulo(radio):
    area = 3.14159 * radio**2
    return area

radio = float(input("Ingrese el radio del círculo: "))

area_del_circulo = calcular_area_circulo(radio)
print("El área del círculo con radio", radio, "es:", area_del_circulo)