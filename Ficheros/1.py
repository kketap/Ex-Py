numero = int(input("Ingresa un numero del 1 al 10: "))
nombre_fichero = 'tabla-' + str(numero)  + '.txt'
f = open(nombre_fichero, 'w')
for i in range(1 , 11):
    f.write(str(numero) + 'x' + str(i) + ' = ' + str(numero * i) + '\n')
f.close()