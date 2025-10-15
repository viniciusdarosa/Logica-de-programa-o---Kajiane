estoque = { }

produto = input("Coloque o nome do produto: ")
preco = float(input("Ponha o preço do produto: "))
quant = int(input("Quantos desse produto? "))

estoque[produto] = (preco,quant)
print(estoque)
print(f"Valor total e estoque = {preco*quant}")

#================================================================================

estoque={
    "caneta":(2.50,10),
    "caderno":(15.00,5),
    "borracha":(1.00,20)
}
p = input("qual o produto que você deseja conferir? ")
for i in estoque.keys():
    if i == p:
        v,f = estoque[i]
        vf = v * f
        print(vf)