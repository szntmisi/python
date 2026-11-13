#1 Olvasd be az adatokat egy megfelelő adatszerkezetbe!
#2 Hány könyv van nyílvántartva?
#3 Mennyi J.K Rowlings könyvek átlagoldalszáma?
#4 Van e  Jiles Veina által írt könyv , ha igen mi a címe ?
#5 Oldalszám szerint rendezd be a könyvcímet 


#1

"""
konyvek = []

with open ( 'doga2.txt', 'r',encoding='utf-8') as fin:
    fin.readline
    for sor in fin:
        seged_lista = sor.strip().split(';')
        konyvek.append(
            "konyvcim" = seged_lista[0]
            "szerzo" = seged_lista[1]
            "oldalszam" = int(seged_lista[2])
        )
#4
i = 0
while i < len(konyvek) and not (konyvek[2] == "Jiles Veina"):
    i += 1

Van i > len(konyvek) 
print(f"{if Van "Van Benne Jiles" else "Nincs Benne"}")


"""
konyvek = []
with open ("doga2.txt","r",encoding='UTF-8') as fin :
    fin.readline()
    for sor in fin:
        seged_lista = sor.strip().split(",")
