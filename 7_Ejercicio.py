def encontrar_min_max(lista):
    if not lista:
        return None, None  # Devolvemos None si la lista está vacía

    minimo = maximo = lista[0]

    for numero in lista:
        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero
    return minimo, maximo

lista_numeros = [12, 89, 1, 10, 90, 41]
minimo, maximo = encontrar_min_max(lista_numeros)
print(f"El número más pequeño es: {minimo}")
print(f"El número más grande es: {maximo}")