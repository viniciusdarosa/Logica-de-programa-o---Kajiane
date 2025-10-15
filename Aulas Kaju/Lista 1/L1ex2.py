tempc = float(input('Digite o grau em celsius: '))

escolha = int(input('\n1-Kelvin(K) \n2-Réamur(Re) \n3-Fahrenheit(F)\n\nEscolha uma opção de conversão: '))

match escolha:
    case 1:
        print(f'A temperatura em graus Kelvin é: {tempc + 273.15}°K') 
    case 2:
        print(f'A temperatura em graus Réamur é: {tempc * 0.8}°Re')
    case 3:
        print(f'A temperatura em graus Fahrenheit é: {tempc*1.8 + 32}°F')
    case _:
        print(f'opção inválida')
