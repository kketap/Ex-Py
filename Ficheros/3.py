numero = int(input('Introduce un numero del 1 al 10: '))
mero = int(input('Introduce un numero del 1 al 10: '))

nombre_fichero = 'tabla-' + str(numero) + '.txt'

try:
    with open(nombre_fichero, 'r') as f:
        lineas = f.readlines()
    print(lineas[mero - 1])
except FileNotFoundError:
    print("Error")