def square(*sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una secuencia de números separados por comas.
    Devuelve una lista con los cuadrados de los números de sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

def statistics(*sample):
    """Función que calcula la media, varianza y desviación típica de una muestra de números.
    Parámetros
    sample: Es una secuencia de números separados por comas.
    Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
    """
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square(*sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics(1, 2, 3, 4, 5))

print(statistics(2.3, 5.7, 6.8, 9.7, 12.1, 15.6))