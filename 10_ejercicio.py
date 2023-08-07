def factorial_iterativo(n):
    if n < 0:
        return None  
    if n == 0 or n == 1:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numero = int(input("Ingresa un número: "))
resultado = factorial_iterativo(numero)

if resultado is None:
    print("No se puede calcular el factorial de un número negativo.")
else:
    print(f"El factorial de {numero} es {resultado}")