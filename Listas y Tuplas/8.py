palabra = input("Escribe una palabra: ")
reversed_palabra = palabra
palabra = list(palabra)
reversed_palabra = list(reversed_palabra)
reversed_palabra.reverse()
if palabra == reversed_palabra:
    print("Es un polindromo")
else :
    print("No es un polindromo")