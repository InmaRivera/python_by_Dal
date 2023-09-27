frase = input("Dime una frase y te calculo cuanto tardarías en decirlo: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(
    f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(
    f'Dalto lo diría en {cantidad_de_palabras*100 //2*1.3 /100} segundos')

if cantidad_de_palabras > 120:
    print('para flaco tampoco te pedí el testamwento')
