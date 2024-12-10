# 4. típus: Dictionary műveletek

"""
Feladat: Adj hozzá egy új kulcs-érték párt egy meglévő dictionary-hez.
Input:
adatok = {"név": "Gábor", "kor": 28}
uj_kulcs = "város"
uj_ertek = "Debrecen"
Elvárt eredmény: {"név": "Gábor", "kor": 28, "város": "Debrecen"}
"""

#
# Első megoldás
#

adatok = {
    "név": "Gábor", 
    "kor": 28
    }

adatok["város"] = "Debrecen"
print(adatok)

#
# Második megoldás
#

adatok.update({"város" : "Debrecen"})
print(adatok)

####################################################################################################################################

"""
Feladat: Módosíts egy meglévő kulcs értékét egy dictionary-ben.
Input:
diak = {"név": "Zsófi", "osztály": 10, "pontszám": 85}
kulcs = "pontszám"
uj_ertek = 90
Elvárt eredmény: {"név": "Zsófi", "osztály": 10, "pontszám": 90}
"""

#
# Első megoldás
#

diak = {
    "név": "Zsófi", 
    "osztály": 10, 
    "pontszám": 85
    }
diak.update({"pontszám" : 90})
print(diak)

#
# Második megoldás
#

diak["pontszám"] = 90
print(diak)

####################################################################################################################################

"""
Feladat: Egy meglévő dictionary-be adj hozzá két új kulcs-érték párt egyszerre.
Input:
profil = {"név": "Anna"}
uj_adatok = {"kor": 22, "ország": "Magyarország"}
Elvárt eredmény: {"név": "Anna", "kor": 22, "ország": "Magyarország"}
"""

#
# C) Feladat
#

profil = {
    "név": "Anna"
    }
uj_adatok = {
    "kor": 22, 
    "ország": "Magyarország"
    }

profil.update(uj_adatok)
print(profil)




