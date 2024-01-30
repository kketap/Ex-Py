def funcion_lista(funcion,lista):
    l = []
    for i in lista:
        l.append(funcion(i))
    return l

def cuadrado(n):
    return n ** 2
print(funcion_lista(cuadrado,[1,2,3,4]))

def cubo(n):
    return n ** 3
print(funcion_lista(cubo,[1,2,3,4]))

def cuartaPotencia(n):
    return n ** 4
print(funcion_lista(cuartaPotencia,[1,2,3,4]))

def quintaPotencia(n):
    return n ** 5
print(funcion_lista(quintaPotencia,[1,2,3,4]))