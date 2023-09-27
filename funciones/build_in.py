
numeros = [4, 7, 1, 42, 15]
# encontrado el numero más alto en una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)  # 42

# buscar el numero más bajo
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)  # 1

# Round redondeando a 6 decimales
# con el 2 añade el numero de decimales detras de la coma, por defecto es 0
numero = round(12.3445, 1)
print(numero)

# devuelve False -> si es 0, vacio, False, none\ True -> distinto a 0, True,cadena o datos no vacíos
resultado_bool = bool(['hola'])
print(f'Resultado con bool: {resultado_bool}')

# all retorna True si todos los valores son verdaderos
resultado_all = all(["true", 234, [133]])
print(f'Resultado con all: {resultado_all}')

# suma todos los valores del iterable, tiene que ser numeros porque sino da errores
suma_total = sum(numeros)
print(f'Resultado de sum: {suma_total}')
