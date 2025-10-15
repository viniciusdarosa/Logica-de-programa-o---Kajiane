n = []
v = []
a = []

cidades = {}

for i in range(2):

    nome = input("Qual o nome da cidade? ")
    nvp = int(input("número de carros de passeio: "))
    na = int(input("número de acidentes: "))

    n.append(nome)
    v.append(nvp)
    a.append(na)

cidades["nome"] = n
cidades["nvp"] = v
cidades["na"] = a

for i in range(2):
    if cidades["na"][i] == max(cidades["na"]):
        print(f"A cidade com maior indície ({max(cidades["na"])}) de acidentes é a cidade {cidades["nome"][i]}")
    if cidades["na"][i] == min(cidades["na"]):
        print(f"A cidade com menor indície ({min(cidades["na"])}) de acidentes é a cidade {cidades["nome"][i]}")

print(f"a média do veiculo das 5 cidades é {sum(v)/len(n)}")

cont=0
nt=0 

for i in range(2):
    if cidades["nvp"][i] <= 2000:
        cont += 1
        nt += cidades["na"][i]

print(f"a média de acidentes de transito nas cidades com menos 2000 veiculos é de {nt/cont}")

    