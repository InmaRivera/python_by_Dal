# Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivo_problemas_resueltos\\datos.csv")
# convertimos a string los datos de una columna
df['edad'] = df['edad'].astype(str)
# mostrar el tipo de dato del primer elemento de la columna edad
print(type(df['edad'][0]))
# reemplazando los datos de dalto por maestro
df['apellido'].replace("dalto", "maestro", inplace=True)
print(df['apellido'])
# eliminamos las ilas con datos faltantes
df = df.dropna()

# eliminamos las filas repetidas
df = df.drop_duplicates()
# creando un csv con el dataframe resultante limpio
df.to_csv("archivo_problemas_resueltos\\datos_limpios.csv")
print(df)
