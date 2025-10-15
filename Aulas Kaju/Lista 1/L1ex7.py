nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso/altura**2
if imc < 18.5:
    print(f"{nome}, abaixo do peso")
elif imc < 25:
    print(f"{nome}, peso normal")
elif imc <30:
    print(f"{nome}, acima do peso")
elif imc > 30:
    print(f"{nome}, obeso")