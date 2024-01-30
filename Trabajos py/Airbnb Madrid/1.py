from urllib import request
from urllib.error import URLError

try :
    f = request.urlopen('http://aprendeconalf.es/python/trabajos/datos/madrid-airbnb-listings-small.csv') #URL expirada

except URLError:
    print("La url ya no existe")

else :
    lineas = f.read().decode('utf-8').splitlines()

    columnas = lineas[0].split('\t')

    seleccion = ['id', 'host_id', 'neighbourhood_group_cleansed', 'accommodates', 'price']
    traduccion = {'id':'id', 'host_id':'anfitrion', 'neighbourhood_group_cleansed':'distrito', 'accommodates':'plazas', 'price':'precio'}

    alojamientos = []

    for linea in lineas[1:]:
        alojamiento = {}
        campos = linea.split('\t')

        for i in range(len(columnas)):
            if columnas[i] in seleccion:
                alojamiento[traduccion[columnas[i]]] = campos[i]
        alojamientos.append(alojamiento)
    print(alojamientos)

def alojamientosDistritos(alojamientos):
    
    alojamientoDistritos = {}
    for alojamiento in alojamientos:
        if alojamiento['distrito'] in alojamientoDistritos.keys():
            alojamientoDistritos[alojamiento['distrito']] += 1
        else :
            alojamientoDistritos[alojamiento['distrito']] = 1
    return alojamientoDistritos

print(alojamientosDistritos(alojamientos))

def filtrarPlazas(alojamientos , plazas):

    return [alojamiento for alojamiento in alojamientos if int(alojamiento['plazas']) >= plazas]

filtro = filtrarPlazas(alojamientos , 10)
print(filtro)

def alojamientosBaratos(alojamientos, distrito, n):
    alojamientosDistrito = [alojamiento for alojamiento in alojamientos if alojamiento['distrito'] == distrito]

    def orden(alojamiento):
        return float(alojamiento['precio'][1:])

    rankingAlojamientos = sorted(alojamientosDistrito, key=orden)
    
    return rankingAlojamientos[:n]

top_arganzuela = alojamientosBaratos(alojamientos , 'Arganzuela' , 10)
print(top_arganzuela)

def alojamientosAnfitriones(alojamiento):
    
    alojamientoAnfitriones = {}

    for alojamiento in alojamientos:
        
        if alojamiento['anfitrion'] in alojamientoAnfitriones.keys():
            alojamientoAnfitriones[alojamiento['anfitrion']] += 1
        
        else :
            alojamientoAnfitriones[alojamiento['anfitrion']] = 1
    
    return alojamientoAnfitriones 

anfitriones = alojamientosAnfitriones(alojamientos)

print(anfitriones)