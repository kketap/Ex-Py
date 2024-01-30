print("OPERATIVA CUENTA BANCARIA")
saldo = 0
operaciones = []

while True:
    print("¿Qué deseas hacer?")
    print("1- Ingreso")
    print("2- Reintegro")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        cantidad = float(input("Ingresa una cantidad: "))
        operaciones.append(cantidad)
        saldo += cantidad
        print("Saldo: ", saldo)

    elif opcion == "2":
        cantidad = float(input("Ingresa una cantidad: "))
        if saldo < cantidad:
            print("No hay saldo suficiente")
        else :
            print("Saldo",saldo)
    else :
        break

ingresos = []
reingresos = []

for i in operaciones:
    if i < 0 :
        reingresos.append(i)
    else :
        ingresos.append(i)

print("Ingresos: ", ingresos)
print("Reintegros:", reingresos)