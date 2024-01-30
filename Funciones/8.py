def func(*listar):
    lista = []
    for i in listar:
        lista.append(i**2)
    return lista

def estadistica(*listar):
    valores = [float(i) for i in listar]
    stat = {}
    stat['media '] = sum(listar) / len(listar)
    stat['varianza'] = sum(func(*listar)) / len(listar) - stat['media '] **2
    stat['desviación tipca'] = stat['varianza'] ** 0.5
    return stat
print(estadistica('1, 2, 3, 4, 5'))

print(estadistica('2.3, 5.7, 6.8, 9.7, 12.1, 15.6'))
