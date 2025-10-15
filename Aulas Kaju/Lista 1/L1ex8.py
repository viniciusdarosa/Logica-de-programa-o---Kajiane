vot = int(input("Quantos votantes são? "))
cont1 = 0
cont2 = 0
cont3 = 0
for i in range(vot):
    nome = input("Qual o seu nome? ")
    cand = int(input("Qual o candidato q você escolhe?\n1 - Deodoro\n2 - Floriano\n3 - Iza\n qualquer outro para voto nulo: "))
    match cand:
        case 1:
            print("Você votou no Deodoro")
            cont1 += 1
        case 2:
            print("Você votou no floriano")
            cont2 += 1
        case 3:
            print("Você votou na Iza")
            cont3 += 1
        case _:
            print("Voto nulo")

print(f"Deodoro teve {cont1} votos")
print(f"Floriano teve {cont2} votos")
print(f"Iza<3 teve {cont3} votos")
            
        