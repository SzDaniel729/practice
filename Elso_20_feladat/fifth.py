# 5. típus: if-else gyakorló feladatok

"""
Feladat: Döntsd el, hogy egy szám pozitív, negatív, vagy nulla, és írd ki a megfelelő üzenetet.
Input:
szam = -5
Elvárt eredmény: "A szám negatív."
"""

szam = -5

if szam > 0:
    print("A szám pozitÍv")
elif szam < 0:
    print("A szám negatív")
else:
    print("A szám nulla")

##########################################################################################################################################################

"""
Feladat: Egy hőmérsékleti érték alapján állapítsd meg, hogy hideg, kellemes vagy meleg van.
Input:
homerseklet = 25
Feltételek:
Hideg: < 15
Kellemes: 15-25
Meleg: > 25
Elvárt eredmény: "Kellemes az idő."
"""

homerseklet = 25

if homerseklet > 25:
    print("Meleg az idő")
elif homerseklet < 15:
    print("Hideg az idő")
else:
    print("Kellemes az idő")

##########################################################################################################################################################

"""
Feladat: Állapítsd meg, hogy egy diák átment-e a vizsgán (>=50 pont), vagy megbukott.
Input:
pontszam = 47
Elvárt eredmény: "A diák megbukott.
"""

pontszam = 47

if pontszam >= 50:
    print("A diák átment a vizsán.")
else:
    print("A diák megbukott")
