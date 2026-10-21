#adatszerkezet:listaban szótárak
#[
#   {"nev": "Tibi","tantargy": "matematika", "jegy": 3}
#   {...}   
#]
#kinek van a legjobb jegye?
tanulok = []
with open ("adatok5.txt","r",encoding="utf-8") as fin:
    fin.readline()
    for sor in fin:
        seged_lista = sor.strip().split(";")
        tanulo={"nev":seged_lista[0],"tantargy":seged_lista[1],"jegy":int(seged_lista[2])}
        tanulok.append(tanulo)
jo_tanulo = tanulok[0]
for tanulo in tanulok:
    if tanulo["jegy"] > jo_tanulo["jegy"]:
        jo_tanulo = tanulo
print(f"A legjobb tanulo neve : {jo_tanulo["nev"]} tantárgya : {jo_tanulo["tantargy"]} jegye: : {jo_tanulo["jegy"]}")