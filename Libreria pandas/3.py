import pandas as pd

def aprobados(notas):
  notas = pd.Series(notas)
  return notas[notas >= 4 ].sort_values(ascending=False)

notas = {'Juan':7, 'María':6.7, 'Pedro':4, 'Carmen': 3.5, 'Luis': 5}
print(aprobados(notas))