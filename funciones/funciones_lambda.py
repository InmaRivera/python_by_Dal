numeros = [1, 2, 4, 4, 5, 6, 7, 8, 9]

# lambda es el nombre de la funcion = lambda parametro por 2


def multiplicar_por_dos(x): return x*2


print(multiplicar_por_dos(5))
# creando una funcion comun que diga si es par o no


def es_par(num):
    if (num % 2 == 0): #si queremos impares en vez de 0 es 1io
        return True

# usando filter con una funcion comun
numeros_pares = filter(es_par, numeros)

print(f'Resultado de numeros pares: {list(numeros_pares)}')#me devuelve la lista de numeros pares


#forma más sencilla de hacer lo anterior, codigo más limpio
numeros_pares_lambda = filter(lambda numero:numero%2 == 0, numeros)
print(f'Resultado con lambda: {list(numeros_pares_lambda)}')