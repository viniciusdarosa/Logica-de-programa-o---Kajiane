frase = input("Digite uma palavra: ").strip()
palavra = frase.split()

repet = {}
for i in palavra:
    if i not in repet:
        repet[i] = 1
    else: 
        repet[i] += 1

print(repet)