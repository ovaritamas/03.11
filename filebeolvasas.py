from allat import *
from emlos import *

allatok = []
allat = None

with open('adatok/allatok.txt', 'r', encoding='utf-8') as f:
    next(f)
    for sor in f:
        nev, faj, eletkor, szorzet_szine = sor.strip().split(",")

        if faj == "kutya":
            allat = Kutya(nev, int(eletkor), "udvar", szorzet_szine)

        elif faj == "macska":
            allat = Macska(nev, int(eletkor), "udvar", szorzet_szine)

        elif faj == "madar":
            allat = Madar(nev)

        elif faj == "keteltu":
            allat = Keteltu(nev)
        
        elif faj == "hullo":
            allat = Hullo(nev)
        allatok.append(allat)

for allat in allatok:
    print(allat)
        