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
# def osszegzes(lista):-----------------------------------------------------------------------------------
#     """összeadja a listá-ban lévő számokat"""
#     osszeg = 0
#     for szam in lista:
#         osszeg += szam

#     return osszeg

# print(osszegzes(szamok))
# print(sum(szamok))
# #add meg a szémok átlagát!
# szamok = [5, 5, 7]
# print(f"a számok átlaga:{osszegzes(szamok) / len(szamok):.2f}")

# from statistics import mean 
# print(mean(szamok))

# #megszámolás hány darab páros szám van a megadott számok között
# szamok = [5, 6, 7, 8]

# db = 0 
# for szam in szamok:
#     if szam % 2 == 0  :
#         db +=1

# print(f"páros számok : {db}.")



# #gyakorló feladat add meg a páros számok átlagát
# paros_db = 0
# szamok = [5, 6, 7, 8, 3, 2, 5, 4, 9]
# paros_osszeg = 0
# for szam in szamok:
#     if szam % 2 == 0:
#         paros_db += 1
#         paros_osszeg += szam

# print(f"páros számok átlaga: {paros_osszeg / paros_db:.2f}.")--------------------------------------------
#eldöntés
# lehetséges válaaszok:van,nincs,mind ilyen,egy ilyen sincs 
#visszatérési érték az egy logikai érték
#pl: van e páros szám a listában?,a listában minden szám páros?...
#kérdés be kell a járni a listát?
#van e páros szám a listában?
szamok = [ 4,5, 7, 9,]

i = 0
while i < len(szamok) and not(szamok[i] %2 == 0):
    i += 1
van = i < len(szamok)
print(f"{'van'if van else  'nincs'} páros szám a listában")

#minden szám páratlan e?
szamok = [5, 4, 7, 9,]

i = 0
while i < len(szamok) and not(szamok[i] %2 == 0):
    i += 1

van = i < len(szamok)
print(f"{'Nem minden'if van else 'Minden'} szám páratlan")

#eldöntés  V2
#van e páros szám a listában
van = False 

for szam in szamok:
    if szam %2 == 0:
        van = True
        break

print(f"{'van'if van else  'nincs'} páros szám a listában")

#kiválasztás tétele
#ha biztosan tudjuk hogy van olyan elem akkor adjuk meg a sorszámot
#vissza térési érték: egy sorszám,ami a addot tulajdonsága elem a listában
#példa: hanyadik ember a legmagasabba listában
# hanyadik elem az első páros szám 
szamok = [4, 7, 5, 9,]
i = 0
while not (szamok[i] %2 == 0):
    i += 1

print(f"az első páros elem indexe a(z):{i},értéke {szamok[i]}")
