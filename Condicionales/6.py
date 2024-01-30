sexo = input("Ingresa tu sexo: ")
nombre = input("Ingresa tu nombre: ")

if sexo == "Mujer" :
    if nombre.lower() < "m":
        group = "A"
    else :
        group = "B"
else :
    if nombre.lower() > "n":
        group = "A"
    else :
        group = "B"
print("Tu grupo es: ",group)
      
   
