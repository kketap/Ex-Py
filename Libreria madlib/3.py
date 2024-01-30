import pandas as pd
import matplotlib.pyplot

def evolucion_ventas(ventas , tipo):
  graficos = {'lineas':'line' , 'barras':'bar','sectores':'pie','area': 'area'}
  fig , ax = plt.subplots()
  ventas.plot(kind = graficos[tipo] , ax = ax)
  plt.title('Evolución del número de ventas')
  return ax

df_ventas = pd.Series([1200 , 840 , 1325 , 1280, 1500], index = [2000, 2001, 2002, 2003, 2004])

evolucion_ventas(df_ventas , 'lineas')
plt.show()
evolucion_ventas(df_ventas , 'area')
plt.show()
evolucion_ventas(df_ventas , 'barras')
plt.show()
evolucion_ventas(df_ventas , 'sectores')
plt.show()
