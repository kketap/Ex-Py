def generarTabla(n):

    nombreFichero = "tabla-" + str(n) + ".txt"

    f = open(nombreFichero , 'w')

    for i in range(n + 1):
        for j in range(n + 1):

            f.write(str(i * j) + "\t")

        f.write("\n")

    f.close()

    return

def leerTabla(n):

    nombreFichero = "tabla-" + str(n) + ".txt"

    print("Contenido del fichero " + nombreFichero + ":")

    try :

        fichero = open(nombreFichero , 'r')
    
    except FileNotFoundError:
         print("El fichero no existe")
    
    else :

        print(fichero.read())

        fichero.close()

n = int(input("Introduce un número entero entre 1 y 10: "))

generarTabla(n)

leerTabla(n)