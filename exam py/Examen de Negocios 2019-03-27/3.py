palabra = input("Ingresa una palabra: ")
palabra = list(palabra)

solucion = list('*' * len(palabra))

fallos = 0

while any(palabra) and fallos < 5:
    letra = input("Introduce una letra: ")
    if letra in palabra:
        print("Acierto")

        i = palabra.index(letra)

        palabra[i] = False

        solucion[i] = letra 
    
    else :
        print("Fallo")

        fallos += 1
    
    print(solucion)

if fallos == 5 :
    print("Perdiste")

else :
    print("Ganaste")
