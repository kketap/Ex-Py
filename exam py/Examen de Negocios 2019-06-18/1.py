nota1 = float(input("Introduce la nota del primer semestre: "))
nota2 = float(input("Introduce la nota del segundo semestre: "))

if nota1 >= 4 and nota2 >= 4 and ((nota1 + nota2) / 100) >= 4:
    print("Has Aprobado")

else :
    print("Has suspendido")
    
    if nota1 < 4:
        print("Tienes que repetir el primer parcial")
    if nota2 < 4 :
        print("Tienes que repetir el segundo parcial")