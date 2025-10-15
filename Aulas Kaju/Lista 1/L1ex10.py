print("Tabela de desconto\nAlcool: 20>litros - 5% and 20<litros - 3%\nGasolina:  20>litros - 6% and 20<litros - 4%")

op = int(input("escolha um tipo de combustível\n1-Alcool\n2-Gasolina"))
A = 4.22
G = 5.65
litro = float(input("Quantos litros? "))
match op:
    case 1:
        if litro>20:
            print(f"o valor final é: R${A*litro - A*litro*5/100}")
        else:
                print(f"o valor final é: R${A*litro - A*litro*3/100}")
    case 2:
        if litro>20:
            print(f"o valor final é: R${G*litro - G*litro*5/100}")
        else:
                print(f"o valor final é: R${G*litro - G*litro*3/100}")