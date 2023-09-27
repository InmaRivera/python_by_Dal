# permiso de escritura con W de write
with open("archivos\\texto_de_Dalto.txt", 'a', encoding="utf-8") as archivo:
    # agregando un archivo
    archivo.write("Esto es lo ultimo que se añadió a la lista\n")
    # usando un bucle para agregar varias lineas
    for i in range(5):
        archivo.write(f'Agregando linea {i+1} nueva\n')
