# 5. Agenda de Contatos
#  Crie um dicionário onde a chave seja o nome do contato e o valor
# outro dicionário com "telefone" e "email".
# ● Permita ao usuário:
# ● Adicionar contato
# ● Buscar contato por nome
# ● Remover contato
# ● Exibir todos os contatos em ordem alfabética

agenda = {

}
while True:
    op = input('''
========================
Bem Vindo!
a)Adicionar contato
b)Buscar contato por nome
c)Remover contato
d)Exibir todos os contatos em ordem alfabética
=========================''').lower()
    match op:
        case 'a':
            nome = input("Digite o nome do contato: ")
            tel = input("Digite o telefone: ")
            am = input("Digite o email: ")
            agenda[nome] = [tel,am]
            print(agenda)
        case 'b':
            p = input("Qual o nome do contato? ")
            print(agenda[p])
        case 'c':
            p = input("Qual o nome do contato? ")
            agenda[p] = 0
        case 'd':
            print(sorted(agenda))
        case _:
            break