# 3. típus: Lista összevonás ciklusok nélkül

"""
Feladat: Fűzz össze két listát úgy, hogy az eredményben az összes elem szerepeljen.
Input:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
Elvárt eredmény: [1, 2, 3, 4, 5, 6]
"""

#
# Első megoldás
#

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(lista1 + lista2)

#
# Második megoldás
#

ossz_list = lista1 + lista2
print(ossz_list)

#
# Harmadik megoldás
#

lista3 = []
for x in lista1:
    lista3.append(x)
for x in lista2:
    lista3.append(x) 
print(lista3)

#
# Negyedik megoldás
#

lista4 = lista1
lista4.extend(lista2)
print(lista4)


########################################################################################################################################################

"""
Feladat: Adj hozzá egy új elemet egy meglévő listához lista-összevonás segítségével.
Input:
eredeti_lista = ["piros", "kék", "zöld"]
uj_elem = ["sárga"]
Elvárt eredmény: ["piros", "kék", "zöld", "sárga"]
"""

eredeti_lista = ["piros", "kék", "zöld"]
uj_elem = ["sárga"]

#
# Első megoldás
#

elso_megoldas = eredeti_lista + uj_elem
print(elso_megoldas)

#
# Második megoldás
#

masodik_megoldas = []
masodik_megoldas.extend(eredeti_lista)
masodik_megoldas.append(uj_elem[0])
print(masodik_megoldas)

#
# Harmadik megoldás
#

harmadik_megoldas = []
harmadik_megoldas.extend(eredeti_lista)
harmadik_megoldas.append("sárga")
print(harmadik_megoldas)

##############################################################################################################################################################

"""
Feladat: Készíts egy listát, amely két meglévő lista első két-két elemét tartalmazza.
Input:
lista1 = [10, 20, 30]
lista2 = [40, 50, 60]
Elvárt eredmény: [10, 20, 40, 50]
"""

lista1 = [10, 20, 30]
lista2 = [40, 50, 60]

#
# Első megoldás
#

lista_c_1 = []
lista_c_1.extend(lista1[0:2])
lista_c_1.extend(lista2[0:2])
print(lista_c_1)

#
# Második megoldás
#

lista_c_2 = []

if 10 in lista1:
    lista_c_2.append(10)
    if 20 in lista1:
        lista_c_2.append(20)
        if 40 in lista2:
            lista_c_2.append(40)
            if 50 in lista2:
                lista_c_2.append(50)

print(lista_c_2)

#
# Harmadik megoldás
#

lista_c_3 = lista1 + lista2
lista_c_4 = []

for szamok in lista_c_3:
    if szamok == 10:
        lista_c_4.append(10)
    elif szamok == 20:
        lista_c_4.append(20)
    elif szamok == 40:
        lista_c_4.append(40)
    elif szamok == 50:
        lista_c_4.append(50)
print(lista_c_4)




















