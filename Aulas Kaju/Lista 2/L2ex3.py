lista = [("vinícius",16),("Izabely",16),("Roberto",45)]

pmv = ("",0)
for i in lista:
    if i[1] > pmv[1]:
        pmv = i

print(f"a pessoa mais velha é {pmv}")
