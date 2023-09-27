import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("problemas_graficos\\colla_ingresos.csv")
print(df)
# creando el grafico
sns.barplot(x="fuentes", y="ingresos", data=df)
# mostrando el total de ingresos
total_ingresos = df['ingresos'].sum()
# mostrando el total
print(f'El total de ingresos es de: ${total_ingresos} USD')

# mostramos el grafico
plt.show()
