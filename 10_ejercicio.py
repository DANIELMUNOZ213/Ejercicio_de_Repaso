def factorial(numero):
    if numero < 0:
        return None  
    elif numero == 0:
        return 1  

    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i

    return resultado

numero_dado = int(input("ingrese un numero: "))
resultado_factorial = factorial(numero_dado)
if resultado_factorial is not None:
    print(f"El factorial de {numero_dado} es: {resultado_factorial}")
else:
    print("El factorial no está definido para números negativos.")
