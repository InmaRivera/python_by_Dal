diccionario = {
    "nombre": "Inma",
    "apellidos": "Rivera",
    "subs": 120
}

for key in diccionario.items():
    print(key)  # devuelve una tupla

# otra forma
diccionario = {
    "nombre": "Inma",
    "apellidos": "Rivera",
    "subs": 120
}

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es: {value}')  # devuelve una tupla
