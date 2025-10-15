tarefas = []

adicionar = lambda tarefa: tarefas.append(tarefa)

def vizualizar():
    print(tarefas)

atualizar = lambda id,tarefa: tarefas.insert(id,tarefa)

excluir = lambda tarefa: tarefas.remove(tarefa)

while True:
    print("-"*30)
    print('''Escolha uma opção:
          1 - Adicionar tarefas
          2 - Vizualizar
          3 - Atualizar
          4 - Excluir
          5 - Sair''')
    print("-"*30)
    resposta = int(input("Escolha uma opção: "))
    match resposta:
        case 1:
            tarefa = input("Adicione uma tarefa: ")
            adicionar(tarefa)
        case 2:
            print(tarefas)
        case 3:
            id = int(input('Qual o posicionamento dela? '))
            id -=  1
            tarefa = input("Troque a Tarefa tarefa: ")
            atualizar(id,tarefa)
            id +=1
            tarefas.pop(id)
        case 4:
            tarefa = input("Exclua uma tarefa: ")
            excluir(tarefa)
        case 5:
            print('Cabousse')
            break
        case _:
            print('Escolha inválida')

    

