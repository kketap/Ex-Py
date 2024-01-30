from math import sin , cos , tan , exp , log

def aplicar_func(funcRecibe_n , numero) :
    funciones = {'sin':sin ,'cos': cos ,'tan': tan ,'exp': exp ,'log': log}
    result = {}
    for i in range(1,1+numero):
        result[i] = funciones[funcRecibe_n](i)
    return result
def calculadora():
    funcRecibe_n = input("Introduce la funcion: ")
    numero = int(input("Introduce un numero: "))
    for i , j in aplicar_func(funcRecibe_n , numero).items():
        print(i,'\t',j)
    return
calculadora()
