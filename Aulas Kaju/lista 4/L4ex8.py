
import random

def jogo():
    num = random.randint(1,100)
    return num


v = int(input("informe o numero que o programa escolheu: "))

if (v != jogo()):
    print("numero errado")
    print(jogo())