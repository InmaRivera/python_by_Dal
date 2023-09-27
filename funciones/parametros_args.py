# suma sencilla
def suma(a, b):
    return a+b


resultado = suma(5, 3)
print(f"El resultado de la suma simple es: {resultado}")

# si queremos mostrar más, esta forma no es óptima
# def suma(lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados = numeros_sumados + numero
#     return numeros_sumados


# # ya se puede agregar mas numeros
# resultado_lista = suma([5, 3, 4, 5, 5, 43, 2, 6, 33])

# forma optima usando el parametro args con *
def suma(nombre, *numeros):  # se pueden añadir strings tb
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"


resultado_lista = suma("Rosa", 5, 3, 4, 5, 5, 43, 2, 6, 33)
print(resultado_lista)


# usando listas con args, de forma optima
def suma_total(numeros):
    return sum([*numeros])  # convertimos a listas con []


resultado2 = suma_total([5, 3, 4, 5, 5, 43, 2, 6, 33])
print(resultado2)  # es lo mismo
