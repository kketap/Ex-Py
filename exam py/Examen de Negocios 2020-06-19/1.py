def paresImpares(lista):

    pares = []

    impares = []

    for i in lista:
        
        if i % 2 == 0:
            
            pares.append(i)
        
        else :
            
            impares.append(i)
        
    pares.sort()

    impares.sort()

    return pares , impares

lista = [3, 8, 2, 7, 5, 4, 6, 1, 9]

pares , impares = paresImpares(lista)

print("Pares: ",pares)

print("Impares: ",impares)
