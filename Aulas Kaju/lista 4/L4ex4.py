contatos = []

adicionar = lambda contato: contatos.append(contato)

def vizualizar():
    print(contatos)

atualizar = lambda id,contato: contatos.insert(id,contato)

excluir = lambda contato: contatos.remove(contato)

while True:
    print("-"*30)
    print('''Escolha uma opção:
          1 - Adicionar contatos
          2 - Vizualizar
          3 - Atualizar
          4 - Excluir
          5 - Sair''')
    print("-"*30)
    resposta = int(input("Escolha uma opção: "))
    match resposta:
        case 1:
            contato = input("Adicione uma contato: ")
            adicionar(contato)
        case 2:
            print(contatos)
        case 3:
            id = int(input('Qual o posicionamento dela? '))
            id -=  1
            contato = input("Troque a contato contato: ")
            atualizar(id,contato)
            id +=1
            contatos.pop(id)
        case 4:
            contato = input("Exclua uma contato: ")
            excluir(contato)
        case 5:
            print('Cabousse')
            break
        case _:
            print('Escolha inválida')

    

