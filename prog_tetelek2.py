#9 szélsőérték kiválasztása minimum kiválasztás, maximum kiválasztás
szamok = [5, 3, 7, 15, 8, 3]
# minimum = szamok[0]
# for szam in szamok:
#     if minimum > szam:
#         minimum = szam
min_index = 0
for i in range(len(szamok)):
    if szamok[min_index] > i:
       min_index = i

print(f"A legkisebb szám:{szamok[min_index]}")

#HF MEGFORDITANI MAXRA MINDENT --------------HF------------------------------------------------------------------------------
#10 rendezés
for i in range(len(szamok-1)):
    for j in range(i+1,len(szamok)):
        if szamok[i] > szamok[j]:
            szamok[i],szamok[j] = szamok[j],szamok[i]
#11 kiválogatás