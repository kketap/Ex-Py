inversion = float(input("Ingresa la cantidad a invertir: "))
interes = float(input("Ingresa el interes anual: "))
años = int(input("N° de años: "))
capital = round(inversion * (interes / 100 + 1) ** años, 2)
print("La capital final es de: "+str(capital))
