monedas = {'Dolar':'$','Euro':'Є'}
moneda = input("Introduce tu moneda: ")
print(monedas.get(moneda.title(),"La moneda no existe"))