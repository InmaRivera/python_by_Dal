archivo = open("archivos\\texto_de_Dalto.txt", encoding="utf-8")
# leer archivo completo
# archivo = archivo.read()
# para leer linea por linea
lineas = archivo.readlines()
# leer una sola linea o caracteres
lineas = archivo.readline()
# cerramos archivo
archivo.close()

# ahora podemos volver a leer
print(archivo)

# para abrir de nuevo
print(lineas)
