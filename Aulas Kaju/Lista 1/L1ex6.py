nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade <= 16:
    print(f"{nome}, não pode votar")
elif idade <=65 and idade >= 18:
    print(f"{nome}, você é obrigado a votar")
elif idade==16 or idade==17 or idade>65:
    print(f"{nome}, você pode votar se quiser")