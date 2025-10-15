import math

areac = lambda r: (r**2)*3.14

retangulo = lambda base,altura: base*altura

triangulo = lambda base,altura: base*altura/2

r = float(input("Digite o Raio: "))
print(areac(r), " m")

base = float(input("Digite a Base: "))
altura = float(input("Digite a Altura: "))
print(retangulo(base,altura), " m")

base = float(input("Digite a Base: "))
altura = float(input("Digite a Altura: "))
print(triangulo(base,altura), " m")
