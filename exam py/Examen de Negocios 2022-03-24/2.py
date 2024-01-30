meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

dias = {"enero":31, "febrero":28, "marzo":31, "abril":30, "mayo":31, "junio":30, "julio":31, "agosto":31, "septiembre":30, "octubre":31, "noviembre":30, "diciembre":31}

mesLunar = 29.53

print("CALENDARIO LUNAR")
print("Este programa convierte una fecha de un año NO bisiesto a un calendario lunar.")

dia = int(input("Ingrese el dia: "))
mes = input("Ingresa el mes: ")

if mes not in meses:
    print("El mes ingresado no existe")

elif dia < 1 or dia > dias[mes]:
    print("El dia o mes no existe")

else :
    numDias = 0
    for i in meses:
        if i != mes:
            numDias += dia
        else :
            numDias += dia
            break
    
    print("El día", dia, "de", mes, "es el día", numDias, "del año.")
    
    print("Habrán pasado", round(numDias / mesLunar, 2), "meses lunares.")