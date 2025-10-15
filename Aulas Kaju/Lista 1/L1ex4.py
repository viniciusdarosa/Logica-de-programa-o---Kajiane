nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = int(input("Digite seu peso: "))

if idade <= 15:
    print(f"{nome} ,não pode doar")
elif idade <=17 and peso > 55:
    print(f"{nome}  ,você pode doar com a permissão do seu responsavel")
elif idade <= 69 and peso > 60:
    print(f"{nome}  ,você pode doar")
else:
    print(f"{nome}  ,você não pode doar")