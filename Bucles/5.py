inversion = float(input("Ingresa una cantidad a invertir: "))
interes = float(input("Ingresa un interes anual: "))
años = int(input("Ingresa una cantidad de años: "))

for i in range(años):
    inversion *= 1 + inversion / 100
    print("Inversion despues de ",str(i+1)," años",str(round(inversion,2)))

