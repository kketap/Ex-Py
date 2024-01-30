def factorial(numero):
    tmp = 1
    for i in range(numero):
        tmp *= i+1
    return tmp
print(factorial(4))
print(factorial(20))