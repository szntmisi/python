szamok = []
# fin = open("szamok1.txt","r",encoding="utf-8")
# for sor in fin:
#     print(sor.strip())
# fin.close()

#mennyi a beolvasott számok összege

with open("szamok1.txt","r",encoding="utf-8") as fin:
    for sor in fin:
        szamok.append(int(sor.strip()))

print(sum(szamok))