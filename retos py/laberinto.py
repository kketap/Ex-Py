laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

def laberinto(dimension , muros):
    laberinto = []

    for i in range(dimension):
        fila = []

        for j in range(dimension):
            if tuple([i , j]) in muro:
                fila.append('X')
        
        laberinto.append(fila)
    return laberinto

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

lab = laberinto(5 , muro)

for i in lab:
    print(''.join(i))


def recorreLaberinto(laberinto): #fix by chatGPT
    fila = columna = 0
    n = len(laberinto) #cambio
    movimientos = ['Abajo']

    while (fila < n - 1 and columna < n - 1):

        if movimientos[-1] != 'Arriba' and fila + 1 < n and laberinto[fila + 1][columna] != 'X':
            fila += 1
            movimientos.append('Abajo')
        
        elif movimientos[-1] != 'Abajo' and fila - 1 >= 0 and laberinto[fila - 1][columna] != 'X':
            fila -= 1
            movimientos.append('Arriba')
        
        elif movimientos[-1] != 'Izquierda' and columna + 1 < n and laberinto[fila][columna + 1] != 'X':
            columna += 1
            movimientos.append('Derecha')
        
        elif movimientos[-1] != 'Derecha' and columna - 1 >= 0 and laberinto[fila][columna - 1] != 'X':
            columna -= 1
            movimientos.append('Izquierda')
        
        else :
            return "No hay salida"

    return movimientos

lab = laberinto(5, muro)
print("Solucion: ", recorreLaberinto(lab))



"""
def recorreLaberinto(laberinto): #Error del original || "n" no definida
    fila = columna = 0
    n = len(laberinto)
    movimientos = ['Abajo']

    while (fila < n - 1 and columna < n - 1):

        if movimientos[-1] != 'Arriba' and fila + 1 < n and laberinto[fila + 1][columna] != 'X':
            fila += 1
            movimientos.append('Abajo')
        
        elif movimientos[-1] != 'Abajo' and fila - 1 >= 0 and laberinto[fila - 1][columna] != 'X':
            fila -= 1
            movimientos.append('Arriba')
        
        elif movimientos[-1] != 'Izquierda' and columna + 1 < n and laberinto[fila][columna + 1] != 'X':
            columna += 1
            movimientos.append('Derecha')
        
        elif movimientos[-1] != 'Derecha' and columna - 1 >= 0 and laberinto[fila][columna - 1] != 'X':
            columna -= 1
            movimientos.append('Izquierda')
        
        else :
            return "No hay salida"

    return movimientos

lab = laberinto(5, muro)
print("Solucion: ", recorreLaberinto(lab))

"""