nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

if idade <= 2:
    print(f"{nome} Seu nível escolar é: Berçario")
elif idade <= 6:
    print(f"{nome} Seu nível escolar é: Educação infantil")
elif idade <= 10:
    print(f"{nome} Seu nível escolar é: Fundamental nível I")
elif idade <= 15:
    print(f"{nome} Seu nível escolar é: Fundamental nível II")
elif idade <= 18:
    print(f"{nome} Seu nível escolar é: Ensino Médio")
else:
    print(f"valor inválido")
