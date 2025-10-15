import random
pessoa = [20, 39, "40(Lotado)"]

def destinos():
    print("1 - Canada")
    print("2 - Japão")
    print("3 - portugal")

def datas():
    print("1 - 27/10/2025")
    print("2 - 18/11/2025")
    print("3 - 31/12/2025")

def pessoas():
    a = random.choice(pessoa)
    return a

destinos()
int(input("Qual o destino? "))
datas()
int(input("Selecione uma data"))
if pessoas() == "40(Lotado)":
    print("Seu voo esta lotado")
else:
    print(f"Seu voo foi reservado, contém {pessoas()} pessoas")