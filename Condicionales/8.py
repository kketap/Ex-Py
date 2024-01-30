bonificacion = 2400

inaceptable = 0
aceptable = 0.4
meritorio = 0.6

puntos = float(input("Ingresa tu puntaje: "))

if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else :
    nivel = ""

if nivel == "":
    print("Nivel Invalido")
else :
    print("Tu nivel es: " % nivel) #error al q no encontre solucion
    print("Te corresponde cobrar: " % puntos * bonificacion)