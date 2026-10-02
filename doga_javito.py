magassagok=[120, 167, 181, 165]
nevek=["Tibi","Karcsi", "Sanyi", "Géza",]


#a1
fo = 0 
for magassag in magassagok:
    if magassag > 180:
        fo += 1
print(fo)


#ab2
osszeg = 0
db = 0
for magassag in magassagok:
    osszeg += magassag
    db += 1

atlag = ossezg = db
print(f"Az átlag magasság = {atlag:.2f}.")

#a3
i = 0
while i <len(magassagok) and not (magassagok[i] == 167):
    i += 1

van = i < len(magassagok)
print(f"{"Van"if van else "Nincs"} 167cm magas játékos")


# a4 
i = 0
sorszam = 0
while i <len(magassagok) and not (magassagok[i] == 185):
    i += 1

van = i < len(magassagok)
if van:
    print(f"Van 185 cm magas srác akinek a sorszáma : {sorszam}.")
else:
    print("Nincs 185 cm magas srác")

#4b
i = 0
sorszam = 0
while i <len(magassagok) and not (magassagok[i] == 185):
    i += 1

van = i < len(magassagok)
if van:
    print(f"Van 185 cm magas srác akinek a sorszáma : {sorszam}.")
else:
    print("Nincs 185 cm magas srác")
    