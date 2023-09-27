with open("archivos\\texto_de_Dalto.txt"):
    print("hola")

# mejorado, abrimos el archivo con with open
with open("archivos\\texto_de_Dalto.txt", encoding="utf-8") as archivo:
    # leemos el archivo
    contenido = archivo.read()
    # mostramos el archivo
    print(contenido)
# no es necesario cerrarlo con with open
