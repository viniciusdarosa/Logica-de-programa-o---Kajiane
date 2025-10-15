import math
soma = lambda a,b:  a**2 + b**2
def hipo(a,b):
    c = math.sqrt(soma(a,b))
    return c

a = float(input("informe o 1° cateto: "))
b= float(input("informe o 2° cateto: "))

print(hipo(a,b))
