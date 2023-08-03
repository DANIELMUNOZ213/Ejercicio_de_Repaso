def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

lista_numeros = [9, 20, 5, 14, 3]
resultado = suma_lista(lista_numeros)
print(f"La suma de los números en la lista es: {resultado}")
