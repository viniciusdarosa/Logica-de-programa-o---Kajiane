#--------------------------------ex1---------------------------

import math

potencia = lambda x: math.pow(x,2)

n = int(input("Digite um número: "))
print(potencia(n))

#--------------------------------ex2---------------------------

numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x*2, numeros))
print(dobrados)

#--------------------------------ex3---------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
maisqcinco = list(filter(lambda x: x>5, numeros))
print(maisqcinco) 

#--------------------------------ex4---------------------------

alunos = [('Lucas', 17), ('Izabely', 16), ('Vinícius', 16)]
ordenado = sorted(alunos, key=lambda x: x[1], reverse=False)
print(ordenado)

#--------------------------------ex5---------------------------

nomes = ["ana", "Carlos", "bia"]
ordenados = sorted(nomes, key=lambda x: x.lower())
print(ordenados) 
