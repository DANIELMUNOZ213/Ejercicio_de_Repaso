def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=' ')
        print()

def generar_matriz(filas, columnas):
    matriz = []
    contador = 1

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(contador)
            contador += 1
        matriz.append(fila)

    return matriz

filas = int(input("ingrese el numero de filas: "))
columnas = int(input("ingrese el numero de columnas: "))

matriz_generada = generar_matriz(filas, columnas)
imprimir_matriz(matriz_generada)