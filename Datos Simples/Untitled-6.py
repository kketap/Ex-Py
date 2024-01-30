peso = float(input("Ingresa tu peso: "))
estatura = float(input("Ingresa tu estatura: "))
imc = round(peso / (estatura)**2,2)
print("Tu imc es de: ",str(imc))