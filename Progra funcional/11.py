from statistics import mean , stdev

def atipico(muestra):
    media = mean(muestra)
    desviacion = stdev(muestra)
    def funcion(numero):
        puntuacion = (numero - media) / desviacion
        return (puntuacion < -3) or (puntuacion > 3)
    return funcion

def datos_atpicos(muestra):
    return list(filter(atipico(muestra) , muestra))

print(datos_atpicos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]))