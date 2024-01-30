tablero = [ 
    [" ", " ", " "], 
    [" ", " ", " "], 
    [" ", " ", " "], 
] 

def mostrarTablero(tablero):
    for fila in tablero:
        print(fila)
    return True

def ponerFicha(tablero , x , y , ficha):
   if tablero[x - 1][y - 1] == " ":
       tablero[x - 1][y - 1] = ficha
   else :
       print("Esa coordenada ya está siendo utilizada, use una libre.")
   return tablero

def final(tablero):
    
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] != " ":
            return tablero[fila][0]
    
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] != " ":
            return tablero[0][columna]
    
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]
    
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != str(" "):
        return tablero[0][2]
       
    for fila in tablero:
        if " " in fila:
            return ""
    return "Empate"

def preguntarCasilla():
    while True:
        x = int(input("Introduce la coordenada X del 1 al 3: "))       
        y = int(input("Introduce la coordenada Y del 1 al 3: "))
        ficha = input("Introduce 0 para círculo o X para cruz: ")

        if x >= 1 and x <= 3 and y >= 1 and x <= 3:
            if ficha.lower() == "x" or ficha == "0":
                return x , y , ficha
        else:
            print("Por favor introduce unas coordenadas válidas.") 

while True:
    mostrarTablero(tablero)
    print()

    x , y , ficha = preguntarCasilla()
    ponerFicha(tablero , x , y , ficha)

    fin = final(tablero)

    if fin:
        mostrarTablero(tablero)

        if fin == "Empate":
            print("La partida ha terminado en empate")
        else:
            print("La partida ha ganado el jugador con la ficha", fin + ".")
        break
       
      
       
         