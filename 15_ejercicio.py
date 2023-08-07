def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]

cadena_ingresada = input("Ingrese una cadena de texto: ")

if es_palindromo(cadena_ingresada):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
