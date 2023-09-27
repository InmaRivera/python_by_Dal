# permiso de escritura con W de write
with open("archivos\\texto_de_Dalto.txt", 'w', encoding="utf-8") as archivo:
    # sobre escribiendo el archivo
    # archivo.write("jajajaja te la reconquiste")
    archivo.writelines(['Hola maestro como andas?\n', 'misericordia\n'])
