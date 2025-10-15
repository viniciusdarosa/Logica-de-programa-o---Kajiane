nome = input("Nome do produto: ")
quantidade = int(input("Quantas unidades? "))
preco = float(input("Qual o preço do produto? "))
vf = quantidade*preco
print(f"O total do produto {nome} é de R${vf}")
op = int(input("Qual a forma de pagamento que você deseja selecionar?\n1- à vista em dinheiro, recebe 10% de desconto \n2- à vista no cartão de crédito, recebe 5% de desconto \n3- em duas vezes, sem juros \n4- em três vezes, com 5% de juros\n opção: "))
match op:
    case 1:
        print(f"O preço final é de: R${vf - vf*1/10}")
    case 2:
        print(f"O preço final é de: R${vf - vf*5/100}")
    case 3:
        print(f"O preço final é de: 2 vezes de R${vf/2}")
    case 4:
        print(f"O preço final é de: 3 vezes de R${vf/3}")
    case _:
        print(f"Opção inválida")