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