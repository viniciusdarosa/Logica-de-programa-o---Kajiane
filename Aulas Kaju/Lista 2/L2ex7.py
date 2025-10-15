biblioteca = {
    "Quarta asa": ("Rebeca",2020),
    "chingchong": ("Chinês", 1987),
    "It": ("um cara lá", 2002),
}

p = input("qual o nome do livro?")
print(biblioteca.get(p,"Livro não encontrado"))