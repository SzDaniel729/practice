# 1. típus: f-string gyakorlása

"""
Feladat: Készíts egy f-stringet, amely megjeleníti egy név és életkor alapján a következőt: "{név} {életkor} éves."
Input:
nev = "Anna"
eletkor = 25
Elvárt eredmény: "Anna 25 éves."
"""

nev = "Anna"
eletkor = 25


A = f"{nev} {eletkor} Éves."
print(A)

################################################################################################################################

"""
Feladat: Hozz létre egy f-stringet, amely egy termék árát és nevét kombinálja, így: "A(z) {termek} ára {ar} forint."
Input:
termek = "táska"
ar = 5000
Elvárt eredmény: "A(z) táska ára 5000 forint."
"""

termek = "táska"
ar = 5000

B = f"A(z) {termek} ára {ar} forint."
print(B)

################################################################################################################################

"""
Feladat: Egy személy nevét, korát és városát kombináld egy mondatba, például: "{nev} {eletkor} éves és {varos}-ban/-ben lakik."
Input:
nev = "Béla"
eletkor = 34
varos = "Budapest"
Elvárt eredmény: "Béla 34 éves és Budapest-ben lakik."

nev2 = "Béla"
eletkor2 = 34
varos = "Budapest"

"""

#
# C) Első megoldás
#

adatok = {
    "nev" : "Béla",
    "eletkor" : 34,
    "lakhely" : "Budapest"
}
print(adatok['nev'],adatok['eletkor'],"éves és a lakhelye",adatok["lakhely"])

#
# C) Második megoldás
#

adatok.update({"szemelyes_adatok":[]})
adatok['szemelyes_adatok'].extend(('Béla',34,'Budapest'))
string = [str(item) for item in adatok["szemelyes_adatok"]]
ures_string = " "
print(ures_string.join(string[0:2]),"Éves és a lakhelye",adatok["szemelyes_adatok"][2])

#
# C) Harmadik megoldás
#

nev2 = "Béla"
eletkor2 = 34
varos = "Budapest"

C = f"{nev2} {eletkor2} éves és a lakhelye {varos}"
print(C)

#
# C) Negyedik megoldás
#

list = ['Python', 'Swift', 'C++',"Béla",'Red', 'Black', 'Green', 34,'BMW', 'Mercedes', 'Tesla', "Budapest",19, 26, 29,'apple', 'banana', 'orange']

nev3 = "Béla"
eletkor3 = 34
varos2 = "Budapest"

if (nev3 in list) and (eletkor3 in list) and (varos2 in list):
    print(nev3, eletkor3, "éves és a lakhelye",varos2)

#
# C) Ötödik megoldás
#

adatok2 = {
    "nev" : "Béla",
    "eletkor" : 34,
    "lakhely" : "Budapest"
}

print(adatok2['nev'],adatok2['eletkor'],"éves és a lakhelye",adatok2['lakhely'])










