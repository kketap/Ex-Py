def invoice(cantidad, vat=21):
    return cantidad + cantidad * vat / 100
print(invoice(1000,10))
print(invoice(1000))
