from urllib import request
from urllib.error import URLError

try :
    f = request.urlopen('http://aprendeconalf.es/python/trabajos/datos/deuda.csv') #URL expirada

except URLError:
    print("La url ya no existe")

else :
    lineas = f.read().decode('utf-8').splitlines()

    columnas = lineas[0].split(',')

    deudas = {}

    for linea in lineas[1]:

        serie = {}

        campos = linea.split(',')

        for i in range(4 , len(columnas)):

            serie[columnas[i][:6]] = campos[i]
        
        deudas[(campos[1] , campos[3])] = serie

    print(deudas)

def deudaPais(deuda , pais , tipo):

    return deudas[(pais , tipo)]

print(deudaPais(deudas, 'AUS', 'DP.DOD.DLTC.CR.M1.PS.CD'))

def rangoDeudas(deudas , pais , tipo):

    deuda = deudas[(pais , tipo)]

    return {'Minimo' : min(deuda.values()) , 'Maximo' : max(deuda.values())}

print(rangoDeudas(deudas, 'AUS', 'DP.DOD.DLTC.CR.M1.PS.CD'))

def deudaInteraExterna(deudas , pais , fecha):

    deuda_interna = deudas[(pais, 'DP.DOD.DECD.CR.PS.CD')]
    deuda_externa = deudas[(pais, 'DP.DOD.DECX.CR.PS.CD')]

    return {'Deuda Interna' : deuda_interna[fecha] , 'Deuda Externa' : deuda_externa[fecha]}

print(deudaInteraExterna(deudas, 'AUS', '2015Q1'))

def deudaMonedaLocalExtr(deudas , pais , fecha):

    deuda_moneda_local = deudas[(pais, 'DP.DOD.DECN.CR.PS.CD')]
    deuda_moneda_extranjera = deudas[(pais, 'DP.DOD.DECF.CR.PS.CD')]

    return {'Dueda Moneda Local' : deuda_moneda_local[fecha] , 'Deuda Moneda Extranjera' : deuda_moneda_extranjera[fecha]}

print(deudaMonedaLocalExtr(deudas , 'AUS', '2015Q1'))