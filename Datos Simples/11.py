cantPan = float(input("Cantidad de barras de pan que lleva: "))

pan = 3000
dcto = 0.6

panDcto = float(round((pan * cantPan) * dcto,4))
panNorm = pan * cantPan

pregunta = input("La barra de pan esta fresca?:")

if pregunta == "No" :
    print("El precio con decuento es de: ",str(panDcto))
else:
    print("El precio final es de: ",str(panNorm))


   
