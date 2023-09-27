cadena1 = "Hola, soy Inma"
cadena2 = "BienvenidosMaquinola"
cadena3 = "12324"
# dir es una funcion
resultado = dir(cadena1)
print(resultado)

# para ejecutar metodos
# convertir todo en minisculas
resultado1 = cadena1.lower()  # mostrar texto en mayusculas
print(resultado1)
# convertir todo en mayuscula
resultado2 = cadena1.upper()
print(resultado2)

# primera letra en mayuscula
resultado3 = cadena1.capitalize()
print(resultado3)

# buscamos una cadena en otra cadena
# devuelve la posicion donde lo encuentra 0 en este caso
busqueda_find = cadena1.find("Hola")
# si devuelve -1 es porque no existe o no está y los espacios cuentan
print(busqueda_find)

# buscamos una cadena en otra cadena
busqueda_index = cadena1.index("I")
# en index si no encuentra nada no pone -1, nos aparece una excepcion
print(busqueda_index)

# si es numerico devuelve true sino devuelve false
es_numerico = cadena1.isnumeric()
print(es_numerico)  # False
es_numerico1 = cadena3.isnumeric()
print(es_numerico1)  # True
# es una cadena de texto pero numeirc comprueba si tiene numeros

# si es alfanumerico nos devuelve true, sino False
alfanumerico = cadena1.isalpha()
print(alfanumerico)  # False

alfanumerico1 = cadena3.isalpha()
print(alfanumerico1)  # False

# para que alfanumerico devuelva true hay que eliminar los espacios
alfanumerico2 = cadena2.isalpha()
print(alfanumerico2)  # False

# contamos las coincidencias de una cadena dentro de otra, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")
print(contar_coincidencias)

# contamos cuantos caracteres tiene una cadena, len es un metodo
contar_caracteres = len(cadena1)

print(contar_caracteres)

# verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("H")  # true
termina_con = cadena1.endswith("a")  # True

print(termina_con)

# reemplaza un pedazo de a cadena dada por otra
cadena_nueva = cadena1.replace("Inma", "Grogu")
print(cadena_nueva)

# separar cadenas con la cadena que le pasamos, las convierte en lista
cadena_separada = cadena1.split(",")

print(cadena_separada)
