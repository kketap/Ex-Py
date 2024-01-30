nFil = 4
nCol = 5

cine = []

for i in range(nFil):
    cine.append("X" * nCol)

while True:
    print("\nRESERVA DE BUTACAS")

    for i in cine:
        print(i)
    
    fila = int(input("Introduce la fila que deseas: "))
    columna = int(input("Introduce la columna que deseas: "))
    
    if fila > nFil or columna > nCol:
        print("La fila y columna elegidas no son válidas.")
    
    elif cine[fila - 1][columna - 1] == "O":
        print("La butaca elegida está ocupada.")
    
    else :
        cine[fila - 1] = cine[fila - 1][columna - 1] + "O" + cine[fila - 1][columna:]
        print("Reserva realizada")
    if input("¿Desea realizar otra reserva? (S/N): ") != "S":
        break

print("Gracias!")
print(cine)