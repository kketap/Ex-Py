def facturacion(facturas , nif , mes):

    filtro = [factura['cantidad'] * (1 + factura['iva'] / 100) for factura in facturas if (factura['nif'] == nif and factura['mes'] == mes)]

    return {'Num facturas' : len(filtro) , 'Total facturado' : sum(filtro)}

facturas = [{'nif': 'B12345678', 'mes': 'marzo', 'cantidad':1000, 'iva': 10},
            {'nif': 'A98765432', 'mes': 'julio', 'cantidad':500, 'iva': 21},
            {'nif': 'B12345678', 'mes': 'marzo', 'cantidad':2000, 'iva': 21},
            {'nif': 'C02040506', 'mes': 'enero', 'cantidad':200, 'iva': 4},
            {'nif': 'A98765432', 'mes': 'julio', 'cantidad':1500, 'iva': 10},
            {'nif': 'B12345678', 'mes': 'abril', 'cantidad':600, 'iva': 10},
            {'nif': 'B12345678', 'mes': 'marzo', 'cantidad':100, 'iva': 4}]

print(facturacion(facturas, 'B12345678', 'marzo'))
print(facturacion(facturas, 'B12345678', 'abril'))
print(facturacion(facturas, 'B12345678', 'agosto'))