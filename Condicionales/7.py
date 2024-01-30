renta = float(input("Ingresa tu renta anual: "))

if renta < 1000 :
    tipo = 5
elif renta < 2000 :
    tipo = 15
elif renta < 3500  :
    tipo = 20
elif renta < 6000:
    tipo = 30
else :
    tipo = 45
print("tienes que pagar: ", renta * tipo )

