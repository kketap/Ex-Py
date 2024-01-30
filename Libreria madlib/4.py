import pandas as pd
import matplotlib.pyplot as plt

def diagrama_lineas(datos):
  fig , ax = plt.subplots()
  datos.plot(ax = ax)
  ax.set_ylim([0 , max(datos.Ingresos.max() , datos.Gastos.max()) + 500])
  plt.title('Evolución Ingresos y Gastos')
  return ax

datos = {'Mes':['Ene', 'Feb', 'Mar', 'Abr'], 'Ingresos':[4500, 5200, 4800, 5300], 'Gastos':[2300, 2450, 2000, 2200]}
df_datos = pd.DataFrame(datos).set_index('Mes')
diagrama_lineas(df_datos)
plt.show()