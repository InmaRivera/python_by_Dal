import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("problemas_graficos\\pedos.csv")
print(df)
# creando el grafico
sns.lineplot(x="fecha", y="pedos", data=df)
# creando un punto en el pico más alto
plt.plot("12-06", 10, "o")
# mostramos el grafico
plt.show()
