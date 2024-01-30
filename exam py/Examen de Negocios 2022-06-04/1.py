n = int(input("Ingresa un numero impar: "))
m = n // 2

for i in range(1 , m + 1):
    print(" " * (m - i) , "*" * (2 * i - 1))
print("*" * n)

for i in range(m , 0 , -1):
    print(" " * (m - 1) , "*" * (2 * i - 1))