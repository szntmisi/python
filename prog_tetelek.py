# #összegzés tétel
szamok = [5, 6, 7]
# #érték szerinti bejárással
# osszeg = 0
# for szam in szamok:
#     osszeg += szam

# print(osszeg)

#index szerinti bejárással
# osszeg = 0
# for i in range(len(szamok)):
#     osszeg += szamok[i]

# print(osszeg)
#összegzés függvénnyel
def osszegzes(lista):
    """összeadja a listá-ban lévő számokat"""
    osszeg = 0
    for szam in lista:
        osszeg += szam

    return osszeg

print(osszegzes(szamok))
print(sum(szamok))
#add meg a szémok átlagát!
szamok = [5, 5, 7]
print(f"a számok átlaga:{osszegzes(szamok) / len(szamok):.2f}")

from statistics import mean 
print(mean(szamok))

#megszámolás hány darab páros szám van a megadott számok között
szamok = [5, 6, 7, 8]

db = 0 
for szam in szamok:
    if szam % 2 == 0  :
        db +=1

print(f"páros számok : {db}.")



#gyakorló feladat add meg a páros számok átlagát
paros_db = 0
szamok = [5, 6, 7, 8, 3, 2, 5, 4, 9]
paros_osszeg = 0
for szam in szamok:
    if szam % 2 == 0:
        paros_db += 1
        paros_osszeg += szam

print(f"páros számok átlaga: {paros_osszeg / paros_db:.2f}.")
    