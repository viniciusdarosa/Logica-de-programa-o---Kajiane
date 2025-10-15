import random

def jogo():
    num = random.randint(1,100)
    return num

print(jogo())

lista = ["iza","vini","kaji","sla"]

def lista():
    n = random.choice(lista)
    return n

print(lista())

lista2 = [1,2,3,4,5,]

def lista2():
    lista2 = random.shuffle(lista2)
    return lista2