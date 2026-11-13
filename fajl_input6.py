osztaly_tanuloi = []
tanulok = []
with open ("adatok6.txt","r",encoding="utf-8") as fin:
    fin.readline()
    for sor in fin:
        seged_lista = sor.strip().split(";")
        tanulo={"nev":seged_lista[0],"tantargy":seged_lista[1],"jegy":int(seged_lista[2])}
        tanulok.append(tanulo)
print(tanulok)