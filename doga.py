#B csoport
magassagok=[120, 167, 181, 165]
nevek=["Tibi","Karcsi", "Sanyi", "Géza", "Zoli"]
# b1. Hányan vannak a csoportban?
# megszámlálás tétel
# print(f"csoportban a létszám:{len(nevek)}")
letszam = 0
for nev in nevek:
    letszam += 1
print(f"a csoport létszáma:{letszam}")

# a2/b2. Mekkora az átlag magasság?

atlag_magassag = sum(magassagok)/(len(magassagok))
print(f"az átlag magasság a csoportban:{atlag_magassag}cm")

#b3. Van e Karcsi nevű játékos?
# #Eldöntés tétel
i = 0
while i < len(nevek) and not (nevek[i] == "Karcsi"):
    i += 1
van = i < len(nevek)
print(f"{"Van" if van else "Nincs"} Karcsi a Játékosok között")
# b4. Keresd meg Zoli-t a játékok között!
# Keresés tétel
i = 0
sorszam = 0
while i < len(nevek) and not (nevek[i] == "Zoli"):
    i += 1
    sorszam += 1
van = i < len(nevek)
if van:
    print(f"Van zoli a játkosok között a {sorszam + 1}. helyen")
else:
    print("Nincs zoli a játékosok között")

# +ab. Add meg a 181 cm magas játékos nevét
magassagok_i = 0
magassagok_sorszam = 0
while i < len(magassagok) and not(magassagok[i] == 181):
    magassagok_i += 1
    magassagok_sorszam +=1
print()
