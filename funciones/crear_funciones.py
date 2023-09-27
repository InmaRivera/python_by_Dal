# creando una función simple
# def saludar():
#     print("Hola humano como estás?")
# saludar()
# saludar()#lo repite las veces que se añada

# crear una funcion que tenga parámetros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "maestro"
    else:
        adjetivo = "amor"
    print(f' Hola {nombre}, mi {adjetivo} como estas?')


saludar("Valentina", "MujeR")
saludar("Carlos", "Hombre")
saludar("Fran", "no binario")

# crear una funcion que nos devuelva valores
def crear_contraseña_random(num):
    chars= "abdcjrjsks" #lo hacemos String
    num_entero = str(num) #convertir a string el primer numero
    num = int(num_entero[0]) #convertirlo a entero y obtenemos el primero
    c1 = num -2 #como lo creamos a numero entero se pone num
    c2 = num
    c3 = num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña #devolver contraseña en vez de imprimirla para que no lo muestre por contraseña, con return guarda la informacion
password = crear_contraseña_random(3) #dependiendo del numero que escribamos aqui se hace la resta anterior y muestra el caracter para contraseña es decir, 
# 3-2 = 1 seria el caracter b, c2 = 3 sería el caract c y así, -2 empezaría por detrás k y 3 * 2 = 6 contraseña aleatoria
frase = f"Tu contraseña nueva es: {password}" #si queremos ver la contraseña
print(frase)

#######otra forma
# crear una funcion que tenga parámetros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "maestro"
    else:
        adjetivo = "amor"
    print(f' Hola {nombre}, mi {adjetivo} como estas?')


saludar("Valentina", "MujeR")
saludar("Carlos", "Hombre")
saludar("Fran", "no binario")

# crear una funcion que nos devuelva valores
def crear_contraseña_random(num):
    chars= "abdcjrjsks" #lo hacemos String
    num_entero = str(num) #convertir a string el primer numero
    num = int(num_entero[0]) #convertirlo a entero y obtenemos el primero
    c1 = num -2 #como lo creamos a numero entero se pone num
    c2 = num
    c3 = num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num #devolver contraseña en vez de imprimirla para que no lo muestre por contraseña, con return guarda la informacion

#desempaquetando la funcion
password, primer_numero = crear_contraseña_random(8367)#aunque haya más numeros se usa el primero
print( f"Tu contraseña nueva es: {password}" )
print( f"El numero utilizado es: {primer_numero}" )


