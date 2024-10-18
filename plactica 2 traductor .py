# Crear un diccionario de traducción español-inglés
def crear_diccionario():
    # Inicializamos un diccionario vacío
    diccionario = {}
    
    # Solicitamos al usuario que introduzca pares de traducción
    entradas = input("Introduce las palabras en español e inglés (formato: español:inglés), separadas por comas: ")
    
    # Dividimos las entradas en pares utilizando la coma como separador
    pares = entradas.split(",")
    
    # Iteramos sobre cada par de palabras
    for par in pares:
        # Separamos la palabra en español y su traducción en inglés
        español, inglés = par.split(":")
        # Agregamos la traducción al diccionario, eliminando espacios extra
        diccionario[español.strip()] = inglés.strip()
        
    # Devolvemos el diccionario creado
    return diccionario

# Traducir una frase utilizando el diccionario
def traducir_frase(diccionario):
    # Solicitamos al usuario que introduzca una frase en español
    frase = input("Introduce una frase en español: ")
    
    # Separamos la frase en palabras individuales
    palabras = frase.split()
    
    # Inicializamos una lista para almacenar las traducciones
    traduccion = []

    # Iteramos sobre cada palabra en la frase
    for palabra in palabras:
        # Comprobamos si la palabra está en el diccionario
        if palabra in diccionario:
            # Si está, añadimos la traducción a la lista
            traduccion.append(diccionario[palabra])
        else:
            # Si no está, añadimos la palabra original a la lista
            traduccion.append(palabra)  # Dejar la palabra sin traducir

    # Unimos las palabras traducidas en una sola cadena y la devolvemos
    return " ".join(traduccion)

# Programa principal
if __name__ == "__main__":
    # Llamamos a la función para crear el diccionario
    diccionario = crear_diccionario()
    
    # Llamamos a la función para traducir una frase y almacenamos el resultado
    resultado = traducir_frase(diccionario)
    
    # Imprimimos la traducción resultante
    print("Traducción:", resultado)
