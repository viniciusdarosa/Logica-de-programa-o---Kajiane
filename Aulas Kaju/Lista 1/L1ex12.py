nome = input("nome: ")
idade = int(input("idade: "))
valor = float(input("qual o valor do seu plano? "))

if idade < 19:
    print(f"Seu novo preço é R${valor + valor*5/100}")
elif idade < 35:
    print(f"Seu novo preço é R${valor + valor*10/100}")
elif idade < 60:
    print(f"Seu novo preço é R${valor + valor*15/100}")
else:
    print(f"Seu novo preço é R${valor + valor*20/100}")
