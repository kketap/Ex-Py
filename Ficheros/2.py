numero = int(input("Ingresa un numero del 1 al 10: "))
nombre_fichero = 'tabla-' + str(numero)  + '.txt'

try:
    f = open(nombre_fichero, 'r')
except FileNotFoundError:
    print("Error . N° no encontrado")
else:
    print(f.read())
    f.close()

