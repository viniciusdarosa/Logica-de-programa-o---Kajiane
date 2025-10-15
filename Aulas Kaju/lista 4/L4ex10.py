import math

raiz = lambda num: math.sqrt(num)

angulo = lambda num: math.sin(num)

def deci(v):
    p = v+1
    a = v-1
    return p,a


num = int(input("informe um numero: "))
print(raiz(num))

an = int(input("informe um angulo: "))
print(angulo(an))

v = int(input("informe um numero decimal: "))
print(deci(v))