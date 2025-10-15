import math

potencia = lambda x,y: math.pow(x,y)

adicao = lambda a,b: a+b

subtracao = lambda a,b: a-b

multiplicacao = lambda a,b: a*b

def divisao(a,b):
    if b == 0:
        return 'Cálculo impossivel'
    else:
        result = a/b
        return result
    
while True:
    print("-"*30)
    print('''Escolha uma opção:
          1 - Adicao
          2 - Subtração
          3 - Mutplicação
          4 - Divisão
          5 - Potenciação
          6 - Sair''')
    print("-"*30)
    resposta = int(input("Escolha uma opção: "))

    match resposta:
        case 1:
            a = float(input("Digite o Primeiro número: "))
            b = float(input("Digite o Segundo número: "))
            print(adicao(a,b))
        case 2:
            a = float(input("Digite o Primeiro número: "))
            b = float(input("Digite o Segundo número: "))
            print(subtracao(a,b))
        case 3:
            a = float(input("Digite o Primeiro número: "))
            b = float(input("Digite o Segundo número: "))
            print(multiplicacao(a,b))
        case 4:
            a = float(input("Digite o Primeiro número: "))
            b = float(input("Digite o Segundo número: "))
            print(divisao(a,b))
        case 5:
            a = int(input("Digite o Primeiro número: "))
            b = int(input("Digite o Segundo número: "))
            print(potencia(a,b))
        case 6:
            print("Ja foi tarde")
            break
        case _:
            print("Opção inválida")
         
       