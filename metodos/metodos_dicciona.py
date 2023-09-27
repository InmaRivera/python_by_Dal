# estructura similar a los json con 3 datos
diccionario = {
    "nombre": 'Inma',
    "apellidos": 'Rivera',
    "edad": 29
}
claves = diccionario.keys()  # keys nos sirve para iterar
print(claves)

# get devuelve los elementos buscados, no lanza excepcion pero muestra none
claves = diccionario.get("apellidos")
print(claves)

# con clear eliminamos todos los elementos del diccionario
# diccionario.clear()
# print(diccionario)

# pop elimina un elemento del diccionario
diccionario.pop("apellidos")
print(diccionario)

# item obteniendo un elemento de items
diccionario_iterable = diccionario.items()
print(diccionario_iterable)
