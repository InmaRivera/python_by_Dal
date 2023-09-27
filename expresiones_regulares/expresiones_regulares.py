import re
texto = '''Hola maestro, esta es la cadena 1m como estas mi capitan?
Esta es la segunda aaaa linea de texto bbbbbbbb
Y esta es la final definitiva de mi capitan'''
# Haciendo una busqueda simple
# resultado = re.findall("esta", texto)

# \d -> busca digitos numericos del 0 al 9
# resultado = re.findall(r'\d', texto)

# \D -> busca todo menos digitos numeros  del 0 -9
# resultado = re.findall(r'\D', texto)

# \w-> busca caracteres alfanumericos [a-z A-Z 0-9 _]
# resultado = re.findall(r'\w', texto)

# \w-> busca todo menos caracteres alfanumericos [a-z A-Z 0-9 _]
# resultado = re.findall(r'\W', texto)

# # \s-> busca todo espacios en blanco -> espacios, tabs, saltos de linea
# resultado = re.findall(r'\s', texto)
# # \S-> busca todo menos espacios en blanco -> espacios, tabs, saltos de linea
# resultado = re.findall(r'\S', texto)
# # .-> busca todo menos saltos en linea
# resultado = re.findall(r'.', texto)
# # \n-> busca todo saltos en linea
# resultado = re.findall(r'\n', texto)

# \ -> cancelar caracteres especiales
# resultado = re.findall(r'\.', texto)

# armando una cadena que busque un numero seguido de un punto y un espacio
# resultado = re.findall(f'\d\.\s', texto)

# buscar el principio de una linea, buscando hola al principio
# resultado = re.findall(f'^Hola', texto)

# # ^ -> buscar el principio de una linea, buscando hola al principio
# resultado = re.findall(f'^Esta', texto, flags=re.M)
# # S -> buscar el final de una linea, buscando hola al principio
# resultado = re.findall(f'capitan$', texto, flags=re.M)

# # {n} -> busca n cantidad de veces el valor de la izquierda
# resultado = re.findall(r'\d{3}', texto)

# {n,m} -> al menos n, como maximo m
# resultado = re.findall(r'[ab]{1}', texto)

# | busca una cosa o la otra
resultado = re.findall(r'\d{1,4}|Hola', texto)
print(resultado)
