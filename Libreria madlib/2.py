import pandas as pd
import matplotlib.pyplot as plt

def diagramas_ventas(ventas , titulo):
  fig , ax = plt.subplots()
  ventas.plot(kind = 'pie' , ax = ax)
  plt.ylabel('')
  plt.title(titulo)
  plt.savefig(titulo + '.png')
  return
ventas = {'Enero':200, 'Febrero':240, 'Marzo':310}
s_ventas = pd.Series(ventas)
diagramas_ventas(s_ventas , 'Ventas Primer Semestre')