interes = 0.04
cantDepositada = float(input("Ingresa la cantidad que depositaste: "))

primerAño = float(round(cantDepositada * (1 + interes),2))
print("Primer año: ",str(primerAño))

segundoAño = float(round(primerAño * (1 + interes),2))
print("Segundo año: ",str(segundoAño))

tercerAño = float(round(segundoAño * (1 + interes),2))
print("Tercer año: ",str(tercerAño))
