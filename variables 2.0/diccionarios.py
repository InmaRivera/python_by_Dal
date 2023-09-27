# creando diccionarios con dict()
diccionario = dict(nombre="Inma", apellidos="Rivera")

# las listas no pueden ser claves, las tuplas si, tira error
# pero podemos usar frozenset
diccionario = {frozenset(["inma", "river"]): "jajaja"}

# creando diccionarios con fromkeys
diccionario = dict.fromkeys(
    ["nombre", "apellidos", "suscriptores"], "Añadir valor")

print(diccionario)
