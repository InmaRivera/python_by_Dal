# for in Ejemplo:
# se convierte en tupla cambiando corchetes por parentesis
animales = ["perro", "gato", "loro", "cocodrilo"]
for animal in animales:
    # Recorriendo la lista de animales muestra el resultado 1º perro 2 vuelta gato...etc
    print(f'Ahora la variable animal es igual a: {animal}')

# se convierte en tupla cambiando corchetes por parentesis
numeros = [10, 20, 30, 12]

# recorriendo la lista numeros y cada valor multiplicandolo por 4
for numero in numeros:
    resultado = numero * 4
    print(resultado)

# iterar varias listas, meter un for dentro de otro for
for numero, animal in zip(numeros, animales):
    print(f"Recorriendo lista 1: {animal}")
    print(f"Recorriendo lista 2: {numero}")

# forma no optima  de recorrer una lista con su indice
for num in range(10, 20):
    print(f'FORMA NO OPTIMA {num}')

# lo mismo pero de otra manera, forma correcta
for num in range(len(numeros)):
    print(f'forma optima: {numeros[num]}')

# para obtener el indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

# usando elfor/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('el bucle terminó')
