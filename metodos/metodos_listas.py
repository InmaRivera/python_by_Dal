# creamos una lista con list
lista = list(["hola", "Rivera", 34., 70, True])
print(lista)

# len lo vimos en las cadenas devolvia cantidad que hay dentro cntando espacios
cadena = "hola"
resultado = len(cadena)
print(resultado)  # devuelve cantidad de elementos

# en listas es igual devuelve la cantidad de elementos que hay dentro de la lista
cantidad_elementos = len(lista)
print(f"cantidad de elementos: {cantidad_elementos}")

# append para agregar elementos a la lista
agregando_con_append = lista.append("jajajaja")
print(lista)  # llamamos a la lista y añade elemento a la lista
print(agregando_con_append)  # devuelve none, para solucionarlo
# llamamos a la lista directament
lista.append('jajajaja')
print(lista)

# insert tb agrega un elemento a la lista con un indice esxpecifico
lista.insert(2, "toma jako")
print(lista)

# extend agrega varios elementos a la lista
# se agrega al final de la lista y con los corchetes
lista.extend([False, 2030])
print(lista)

# pop elimina un elemento de la lista
# borramos elemento cero, para eliminar el ultimo elemento se usa -1, -2 para eliminar el antepenultimo y asi sucesivamente
lista.pop(-1)
print(lista)

# remove elemina por su valor

lista.remove("toma jako")  # si el parametro no está lanza error
print(lista)

# elimina todos los elementos
# lista.clear()
# print(lista)

# sort ordena los elementos de forma ascendente
# con cadena de texto no funciona
lista_numeros = ([23, 65, 24, 35, 45, 89, 12])
lista_numeros.sort()
lista_numeros.reverse()  # la inversa
print(lista_numeros)
# verificando si un elemento se encuentra en la lista
# busca un  numero que sea igual al de la lista
elemento_encontrado = lista_numeros.index(35)
print(elemento_encontrado)

# las tuplas son inmutables, no se pueden cambiar. solo se puede buscar y usar index
# en los conjuntos con el set se puede copiar y algunas cosas mas que pone ahí
print(dir(set(['dsksdkf', 'kjnvfdkjgkjdz'])))
