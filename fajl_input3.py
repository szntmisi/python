#olvasd be a szamok3.csv számokat és add meg az átlagot?
szamok = []

with open("./Adatok/szamok3.csv","r",encoding="utf-8") as fin:
    sor = fin.readline()
    sor = fin.readline()
    seged_lista = sor.strip().split(";")
    for elem in seged_lista:
        szamok.append(int(elem))
print(szamok)