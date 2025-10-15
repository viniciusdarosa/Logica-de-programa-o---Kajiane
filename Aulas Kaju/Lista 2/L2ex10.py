# 4. Sistema de Estoque Avançado
#  Crie um dicionário chamado estoque onde cada chave é o nome de
# um produto e o valor é outro dicionário com "preço" e
# "quantidade".
# O usuário pode escolher:
#  a) Adicionar produto
#  b) Atualizar quantidade
#  c) Calcular valor total do estoque
#  d) Listar todos os produtos com preço e quantidade
vt = 0
estoque = {

        }
while True:
    op = input('''
=====================================================
Bem vindo!
a) Adicionar um produto
b) Atualizar quantidade
c) Calcular valor total do estoque
d) Listar todos os produtos com preço e quantidade
======================================================
''').lower()

    match op:
        case 'a':
            nome = input("Digite o nome do produto: ")
            quant = int(input("Digite a quantidade: "))
            preco = float(input("Digite o preço: "))
            estoque[nome] = [quant,preco]
            print(estoque)
        case 'b':
            p = input("Qual o nome do produto que você deseja atualizar? ")
            estoque[p][0] = int(input("Atualize a quantidade: "))
            print(estoque[p])
        case 'c':
            for i in estoque:
                q,p = estoque[i]
                vt += q*p
                print(vt) 
            vt = 0
        case 'd':
            print(estoque)
        case _:
            print("acabou")
            break