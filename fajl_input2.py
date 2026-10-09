#olvasd be a szamok2.txt számokat és add meg az átlagot?
szamok = []

with open("szamok2.txt","r",encoding="utf-8") as fin:
    sor = fin.readline()
    seged_lista = sor.strip().split(" ")
    # szamok1 = list(map(int,seged_lista))
    # print(szamok1)
    for elem in seged_lista:
        szamok.append(int(elem))

print(szamok)

from statistics import mean
print(mean(szamok))

print(sum(szamok)/ len(szamok))
