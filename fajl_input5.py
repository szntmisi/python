#adatszerkezet:listaban szótárak
#[
#   {"nev": "Tibi","tantargy": "matematika", "jegy": 3}
#   {...}   
#]
#kinek van a legjobb jegye?
tanulok = []
jo_tanulo = tanulok[0]
for tanulo in tanulok:
    if tanulo["jegy"] > jo_tanulo["jegy"]:
        jo_tanulo = tanulo
print(f"A legjobb tanulo neve : {jo_tanulo["nev"]} tantárgya : {jo_tanulo["tantargy"]} jegye: : {jo_tanulo["jegy"]}")