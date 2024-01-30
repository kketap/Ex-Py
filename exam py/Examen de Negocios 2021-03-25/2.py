combinacion = [7, 13, 21, 37, 46, 50]

fallos = []

for i in range(6):
    num = int(input("Introduce el siguiente número de la combinación ganadora: "))

    if not num in combinacion:
        
        fallos.append(num)

if len(fallos) == 0:
    
    print("Ganaste!")

else :
    print('Los siento, no acertaste los siguientes números:', fallos)
    