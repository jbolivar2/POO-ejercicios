def fac(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


n = int(input("Ingrese un número: "))

for i in range(1, n + 1):
    print("El factorial de", i, "es:", fac(i))
