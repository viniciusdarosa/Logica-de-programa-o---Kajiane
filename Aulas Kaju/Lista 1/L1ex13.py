tarefas = []
while True:
    print('''
      ========MENU========     
1-Adicionar uma tarefa a lista
2-Remover uma tarefa da lista
3-Exibir todas as tarefas
4-Buscar uma tarefa especifica
      =====================
''')
    op = int(input("Escolha uma opção: "))
    match op:
        case 1:
            t = input("Adicione uma tarefa: ")
            tarefas.append(t)
            print(tarefas)
        case 2:
            i = input("Escolha uma tarefa para tirar")
            tarefas.remove(i)
            print(tarefas)
        case 3:
            print(tarefas)
        case 4:
            t = input("Qual o número da que tarefa você procura? ")
            print(tarefas[t])
        case _:
            break