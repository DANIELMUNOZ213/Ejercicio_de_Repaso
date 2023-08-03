import random

def generar_lista_aleatoria(n, minimo, maximo):
    lista_aleatoria = [random.randint(minimo, maximo) for _ in range(n)]
    return lista_aleatoria

n = int(input("Ingrese la cantidad de números aleatorios que desea generar: "))

minimo = int(input("Ingrese el valor mínimo para los números aleatorios: "))
maximo = int(input("Ingrese el valor máximo para los números aleatorios: "))

lista_aleatoria = generar_lista_aleatoria(n, minimo, maximo)

print("Lista de números aleatorios:", lista_aleatoria)