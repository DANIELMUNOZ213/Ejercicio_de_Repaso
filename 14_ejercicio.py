def calcular_media(lista_numeros):
    if not lista_numeros:
        return None  
    
    suma_total = sum(lista_numeros)
    cantidad_numeros = len(lista_numeros)
    
    media = suma_total / cantidad_numeros
    return media


numeros = [12, 25, 10, 8, 15]
media_calculada = calcular_media(numeros)

if media_calculada is not None:
    print("La media aritmética es:", media_calculada)
else:
    print("La lista de números está vacía.")
