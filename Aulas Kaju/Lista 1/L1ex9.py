nome=[]
altura=[]
genero=[]

dados = {"nome:": nome,"altura:": altura,"genero": genero}

amt = 0

for i in range(2):
    nomep = input("Qual o seu nome? ")
    alturap = float(input("Qual a sua altura? "))
    generop = input("Qual o seu gênero? (M) ou (F) ou (NB)")
    print("-"*50)
    nome.append(nomep)
    altura.append(alturap)
    genero.append(generop)
    if genero == 'f':
        amt += altura

print(f"a pessoa com altura máxima tem {max(dados["altura:"])}m e a menor tem {min(dados["altura:"])}m")

f = genero.count("f")
  
print(f"A altura média de mulheres é: {amt/f}")
    
m = genero.count("m")

print(f"O número total de homens é: {m}")

print(f"mulheres {(f/5)*100}%")
print(f"homens {(m/5)*100}%")





