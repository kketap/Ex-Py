import pandas as pd

def estadistica_notas(notas):
  notas = pd.Series(notas)
  estadisticos = pd.Series([notas.min() , notas.max() , notas.mean() , notas.std()] , index = ['Min', 'Max', 'Media', 'Desviación típica'])
  return estadisticos

notas = {'Juan':7, 'María':6.7, 'Pedro':4, 'Carmen': 3.5, 'Luis': 5}
print(estadistica_notas(notas))