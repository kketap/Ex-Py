laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]

def laberinto(dimension, muros):
    ''' Función que construye un laberinto cuadrado de una dimensión dada poniendo.

    Parámetros:
        - dimension: Es un entero con la dimensión del laberinto. 
        - muros: Es una lista de tuplas con las coordenadas (x,y) donde hay muros.

    Salida: 
        Una matriz (lista de listas) que representa el laberinto. 
    '''

    # Creamos una lista vacía para añadir las filas del laberinto.
    laberinto = []
    # Bucle iterativo para añadir las filas del laberinto.
    # i toma valores de 0 a dimension-1 
    for i in range(dimension):
        # Creamos una lista vacía para añadir las casillas de la fila.
        fila = []
        # Bucle iterativo para recorrer las columnas del laberinto.
        # j toma valores de 0 a dimension-1.
        for j in range(dimension):
            # Condicional para comprobar si la tupla está en el la lista de muros.
            if tuple([i, j]) in muro:
                # Si la tupla está en la lista de muros ponemos una X en la casilla.
                fila.append('X')
            else:
                # Si la tupla no está en el muro ponemos un espacio en blanco en la casilla.
                fila.append(' ')
        laberinto.append(fila)
    return laberinto

# Tupla de coordenadas de las celdas con muro en el laberinto
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) 
lab = laberinto(5, muro)   

# Mostrar el laberinto por pantalla
for i in lab:
    print(''.join(i))


def recorreLaberinto(laberinto):
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

