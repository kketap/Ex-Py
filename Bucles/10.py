numero = int(input("Ingresa un numero entero: "))

i = 2

while numero % i:
   i += 1
if i == numero:
   print(str(numero)+" es primo")
else :
   print(str(numero)+" no es primo")