palabra = input("Ingresa una paalabra: ")

n = int(input("Introduce ubs nunero entero positivo"))
        

for i in  (range(len(palabra) - n + 1)):
   print(palabra[i:i+n])