nomes = ["Ana", "Bruno", "Alice", "André", "Carlos", "Augusto", "Isabela"]

nomes_com_a = []
for nome in nomes:
    if nome.startswith("A"):
        nomes_com_a.append(nome)

print(nomes_com_a)