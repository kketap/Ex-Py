cadenaOfertas = "disco duro 500Gb;200;25;15\nmemoria ram 16Gb;500;30;20\nratón inalámbrico;800;12;10\ntarjeta wifi;150;20;12"

listaOfertas = cadenaOfertas.split('\n')

ofertas = {}

for i in listaOfertas:

    info = i.split(';')

    ofertas[info[0]] = info[1:]

for producto , info in ofertas.items():

    if '%' in info[2]:  # Verifica si el descuento está en porcentaje
      precio = float(info[1]) * (1 - float(info[2].strip('%')) / 100)
    else:  # Si no es un porcentaje, consideramos que es un valor absoluto
      precio = float(info[1]) - float(info[2])


    precio = float(info[1]) * (1 - float(info[2]) / 100 )

    print(producto , 'vale' , precio , '$')