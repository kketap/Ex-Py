edad = int(input("Ingresa tu edad: "))
sueldo = int(input("Ingresa tu sueldo liquido mensual: "))

if edad < 18 and sueldo < 1000000 :
    print("No puede pagar impuestos: ")

else :
    print("Puede pagar impuestos")