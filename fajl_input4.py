szamok = []

with open("szamok4.csv","r",encoding="utf-8") as fin:
    fin.readline()
    for sor in fin:
        seged_lista = sor.strip().split(";")
        for elem in seged_lista:
            szamok.append(int(elem))
print(szamok)