frutas = ["banana", "manzana", "ciruela",
          "pera", "naranja", "granada", "durazno"]
cadena = "Hola Inma"
numeros = [2, 4, 5, 6]


for fruta in frutas:
    if fruta == 'granada':  # iene que concordar con la palabra exacta
        continue  # se salta la que hayamos escrito, elimina granada en este caso
    print(f'me voy a comer una: {fruta}')

# evitar que el bucle siga ejecutandose:
for fruta in frutas:
    if fruta == 'naranja':
        break  # termina el bucle
    print(f'me voy a comer una: {fruta}')
else:
    print("terminado")  # no aparece por el break

# recorrer una cadena de texto:
for letra in cadena:
    print(letra)

# for en una sola linea de codigo
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)
    print(numeros_duplicados)

# for en una sola linea de codigo, mejorado(duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
