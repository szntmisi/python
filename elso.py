print("Hello Larp!")

#kérj be egy számot hogy pozitív vagy negatív
"""
változó típusok
1 string
2 szám
3 logikai
str(5) -> "5"

"""
knev = "Mihály"
egesz = 3
tort = 3.14
lany_e = False 
print(lany_e)
print(tort)
print(f"a szám értéke:{egesz}")
print(f"a szám értéke:{tort:.1f}")
#str(5) -> "5"
print(type(str(5)))

#int("5") -> 5
print(type(int("5")))

#float("3.14") -> 3.14
print(type(float("3.14")))

#bool(0) -> False
print(type(bool(0)))

#list()
lista = [1, 1, 9, 5, 6]
print(type(lista))

#set()
halmaz = set (lista)
print(halmaz)

#dict()
szotar = {
    "vnev": "Szántó" ,
    "knev": "Mihály" ,
    "kor" : 18
}
print(type(szotar))

#tuple
t = (1, 10)
print(type(t))
####
szam = int(input("adjon meg egy számot: ") or "13")
if szam<0:
    print(f"a {szam} kisebb mint 0.")
elif szam == 0:
    print(f"a szam a nulla.")
else :
    print(f"a {szam} kisebb mint 0.")

"""
szam=int(input("Kérek egy számot: "))
if szam % 2 ==0:
    print("a szám páros")
else:
    print("a szám nem páros")
"""
