
import datetime


from datetime import datetime, timedelta
agora = datetime.now()
print("Data e hora atuais:", agora)


naci = lambda ano,ano2: ano2 - ano

ano = int(input("informe seu ano de nacimento: "))
ano2 = int(input("informe o ano atual: "))
print(naci(ano,ano2))

def adicionar():
    data = input("Digite uma data : ")

    data2 = datetime.strptime(data, "%d/%m/%Y")

    nova_data = data2 + timedelta(days=15)

    return nova_data.strftime("%d/%m/%Y")

print(adicionar())
