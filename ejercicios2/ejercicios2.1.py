# falto el profe y los pibes van a armar la clase

# Pedir e nombre y la edad de los compañeros que vinieron hoy a clase
def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []  # creamos una lista vacía
    # creamos un bucle que va a ser aleatorio
    for i in range(cantidad_de_compañeros):
        # le pedimos al usuario que meta el nombre
        nombre = input("Indica el nombre del compañero: ")
    # indicamos que indique la edad añadimos int para convertir a entero
        edad = int(input("Indica la edad del compañero: "))
        compañero = (nombre, edad)
    # Añadimos cada compañero a la lista compañeros
        compañeros.append(compañero)
    # ordenamos por edad de menos a mayor 1 es edad
    compañero.sort(key=lambda x: x[1])
    asistente = compañeros[0][0]  # devuelve una tupla con nombre y edad
    profesor = compañeros[-1][0]
    # devolvemos una tupla
    return asistente, profesor


# desempaquetamos lo que nos devuelve la funcion
asistente, profesor = obtener_compañeros(5)
print(f'El profesor es: {profesor} y su asistente es: {asistente}')
