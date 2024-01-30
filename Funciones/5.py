def areaCiculo(radio):
    pi = 3.14
    return pi * radio ** 2
def volumenCilindro(radio, altura):
    return areaCiculo(radio)* altura

print(volumenCilindro(3,5))