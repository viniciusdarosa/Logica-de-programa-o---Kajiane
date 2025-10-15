
cadrasto = {}
def c(nome ,nota):
   cadrasto[f"{nome}"] = nota

def al(nome ):
    for nome in cadrasto:
        if nome not in cadrasto:
            return "erro"
    
def ex(nome):
    for nome in cadrasto:
        if nome in cadrasto:
            r =input(print("deseja excluir esse cadrastro?")) 
            if r == "sim":
                cadrasto[nome] = nota

def e():
    return cadrasto

def cal():
    media = sum(cadrasto)/len(cadrasto)
    return media



while True:
    print("-"*30)
    print("cadastrar nota(c)\nalterar nota(al)\nexcluir nota(ex)\nexibir nota(e)\ncalcular media(cal)\nsair(s)")
    print("-"*30)
    r = input("informe sua resposta: ").lower()

    match r:
        case "c":
            nome = input("informe o seu nome: ")
            nota = float(input("informe a nota: "))
            c(nome ,nota)
        case "al":
            nome = input("informe o nome: ")
            print(al(nome ))
        case "ex":
            print(ex(nome))
        case "e":
            print(e())
        case "cal":
            print(cal())
        case "s":
            print("programa encerrado")
            break