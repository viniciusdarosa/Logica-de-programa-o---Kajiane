notas={
    "Vini": [5,8.9,6],
    "Iza": [9,10,9.7],
    "Mariscleide": [4,2.3,0.1]
}
for i in notas:
    n = sum(notas[i])
    if n/3 >=7:
        print(i," Passou de ano")