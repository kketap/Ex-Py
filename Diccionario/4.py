meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}

fecha = input("Ingresa una fecha: ")

fechaSplit = fecha.split('/')

print(fechaSplit[0], 'de', meses[int(fechaSplit[1])], 'de', fechaSplit[2])
