inicio = int(input("Ingresa el año incial: "))
fin = int(input("Ingresa el año final: "))

años = []
ingresos = []
gastos = []

for i in range(inicio , fin + 1):
    años.append(i)
    ingresos.append(float(input("Ingresa los ingresos del año "+ str(i) + ":")))
    gastos.append(float(input("Ingresa los gastos del año "+ str(i) + ":")))

beneficios = []

for i in range(len(ingresos)):
    beneficios.append(ingresos[i] - gastos[i])
print(beneficios)

hayBeneficio = []

for i in range(len(beneficios)):
    hayBeneficio.append(beneficios[i] > 0)
print(hayBeneficio)

añosBeneficio = []
añosPerdidas = []

for i in range(len(hayBeneficio)):
    
    if hayBeneficio[i]:
        añosBeneficio.append(años[i])
    
    else :
        añosPerdidas.append(años[i])

print('Años con beneficios: ', añosBeneficio)
print('Años con pérdidas: ', añosPerdidas)