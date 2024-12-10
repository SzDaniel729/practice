# 2. típus: Lista műveletek (slicing)

"""
Feladat: Írd ki az első három elemet a listából slicing segítségével.
Input:
szamok = [1, 2, 3, 4, 5, 6]
Elvárt eredmény: [1, 2, 3]
"""

adatok = {

}

adatok.update({"szamok":[]})
adatok["szamok"].extend((1, 2, 3, 4, 5, 6))
print(adatok["szamok"][:3:])

################################################################################################################################

"""
Feladat: Hozz létre egy új listát, amely csak a lista utolsó két elemét tartalmazza.
Input:
szavak = ["alma", "körte", "szilva", "barack"]
Elvárt eredmény: ["szilva", "barack"]
"""

#
# Első Megoldás
#

adatok.update({"szavak":[]})
adatok["szavak"].extend(("alma", "körte", "szilva", "barack"))
adatok["szavak"].remove("alma")
adatok["szavak"].remove("körte")
print(adatok["szavak"])

#
# Második Megoldás
#

szavak = ["alma", "körte", "szilva", "barack"]
szavak2 = []
keresett_str = "szilva"
keresett_str2 = "barack"
if (keresett_str in szavak):
    szavak2.append(keresett_str)
    if (keresett_str2 in szavak):
        szavak2.append(keresett_str2)

print(szavak2)

#
# Harmadik megoldás
#

szavak3 = []
szavak3.extend(("szilva","barack"))
print(szavak3)

################################################################################################################################

"""
Feladat: Írd ki minden második elemet a listából slicing segítségével.
Input:
betuk = ["a", "b", "c", "d", "e", "f"]
Elvárt eredmény: ["a", "c", "e"]
"""

#
# Első megoldás
#

adatok.update({"betuk":[]})
adatok["betuk"].extend(("a", "b", "c", "d", "e", "f"))
print(adatok["betuk"][::2])

#
# Második megoldás
#

betuk = ["a", "b", "c", "d", "e", "f"]
print(betuk[::2])



















