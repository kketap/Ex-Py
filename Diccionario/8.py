diccionario = {}

palabras = input("Ingresa una lista de palabras: ")

for i in palabras.split(','):
    clave,valor = i.split(':')
    diccionario[clave] = valor
frase = input("Ingresa una frase en español: ")
for i in frase.split():
    if i in diccionario :
        print(diccionario[i], end=' ')
    else :
        print(i, end=' ')