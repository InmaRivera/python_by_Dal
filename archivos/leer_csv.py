import pandas as pd
# usando la funcion read_csv para leer el archivo cSv
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")
# obteniendo todos los resultados
# print(df)

# obteniendo los datos de la columna nombre
nombres = df["nombre"]
# print(nombres)

# cadena = "123456789"
# print(cadena[0])

# # indicar lo hasta donde queremos mostrar
# print(cadena[2:5])
# ordenando el dataframe por la edad
# df_ordenado = df.sort_values("edad")
# # ordenando el dataframe por la edad descendente
# df_ordenado = df.sort_values("edad", ascending=False)

# contatenando dos dataframe
df_concatenado = pd.concat([df, df2])

# accediendo a la primera fila con head
primeras_filas = df.head(3)

# accedemos a las fijas de abajo
ultimas_filas = df.tail(3)
# accediendo a la cantidad de filas y columnas con shape
filas_y_columnas = df.shape

# obteniendo datos estadisticos del dataframe
df_info = df.describe()

# accediendo a un elemento especifico con loc, accedemos a la fila 2
elemento_especifico_loc = df.loc[2, "edad"]
# accediendo a la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2, 2]
# accediendo a odos los apellidos con loc
apellidos_loc = df.loc[:, "apellido"]
# accediendo a odos los apellidos con iloc
apellidos_iloc = df.iloc[:, 1]
# accediendo a la fila 3 con loc
fila_3 = df.loc[2, :]
# accediendo a la fila 3 con iloc
fila_3_iloc = df.iloc[2, :]
#accediendo a filas mauor que 30
mayor_30 = df.loc[df["edad"]>30,:]
print(mayor_30)
