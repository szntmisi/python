# d = {
#     "nev":"Marcell",
#     "kor":18,
#     "kolis_e":False
#     }

# print(d)
# print(d["nev"])
# for key in d:
#     print(f"{key}:{d[key]}")
# #hozd létre a tanulok nevű listát amibe minden tanulónaka nevét a korát és kolis-e mezőjét elktárolják
# tanulok = []
# s = None
# while s != "":
#     be_nev = input("Név:")
#     be_kor = int(input("Kor:"))
#     be_kolis_e = bool(int(input("Kolis-e: [0:Nem,1:Igen]")))
#     tanulok.append({
#         "nev":be_nev,
#         "kor":be_kor,
#         "kolis-e":be_kolis_e
#     })
#     s = input("új adatot akarsz e felvennI? [i:Igen,Enter:nem] ")

# print(tanulok)

#kérj be hálozati eszkoz neveket és az eszkoz nevet ipv4 címeket ez 192.168.1.0/24 halozatban legyen ls add meg a legnagyobb hasznalt ip cimet ls az eszkoz nevet
eszkozok = []
# eszkoz1 = {
#     "eszkoz_neve": "edge",
#     "ipv4" : 5
# }
# eszkozok.append(eszkoz1)
# eszkoz2 = {
#     "eszkoz_neve": "R1",
#     "ipv4" : 6
# }
# eszkozok.append(eszkoz2)
# eszkozok.append({
#     "eszkoz_neve": "R2",
#     "ipv4" : 7

# })
be_nev = None
while be_nev != "":
    be_nev = input("Kérem a nevet: [ENTER:VÉGE]")
    if be_nev != "":
        be_ipv4 = int(input("Add meg az eszköz ipv4 címet utolsó oktettjét:"))
        eszkozok.append({
            'eszkoz_neve' : be_nev,
            'ipv4' : be_ipv4
        })

max_index = 0
for i in range(len(eszkozok)):
    if eszkozok[i]["ipv4"] > eszkozok[max_index]["ipv4"]:
        max_index = i
print(eszkozok[max_index])