"""
### Listák és alapvető műveletek
1. Hozz létre egy listát a hét napjaival. Írd ki az első és az utolsó napot a listából.
2. Adj hozzá egy új napot (pl. "Ünnepnap") a lista végéhez, majd töröld ki azt.
3. Írj egy programot, amely összegzi egy számokat tartalmazó lista elemeit.
"""



napok = []
napok.extend(["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"])

################################################################################################################################
# 1. Hozz létre egy listát a hét napjaival. Írd ki az első és az utolsó napot a listából.

#
# 1.) Első megoldás
#

elso_megoldas = []
elso_megoldas.append(napok[0])
elso_megoldas.append(napok[-1])
print(elso_megoldas)

#
# 1.) Második megoldás
#

print(napok[0],napok[-1])

#
# 1.) Harmadik megoldás
#

x = "Hétfő"
y = "Vasárnap"

if x in napok:
    print(x)
if y in napok:
    print(y)


#
# 1.) Negyedik megoldás
#

for item in napok:
    if item == "Hétfő":
        print(item)
    if item == "Vasárnap":
        print(item)

################################################################################################################################
# 2. Adj hozzá egy új napot (pl. "Ünnepnap") a lista végéhez, majd töröld ki azt.

#
# 2.) Első megoldás
#

napok.append("Ünnepnap")
napok.remove("Ünnepnap")

#
# 2.) Második megoldás
#

uj_nap = "Ünnepnap"

if uj_nap not in napok:
    napok.append(uj_nap)

for item in napok:
    if item == "Ünnepnap":
        napok.remove(uj_nap)

################################################################################################################################
# 3. Írj egy programot, amely összegzi egy számokat tartalmazó lista elemeit.



def osszegzes(*args):
    lista = []
    hibak = []       
    for item in args:
        if isinstance(item, int) or isinstance(item, float) or isinstance(item, complex):
            lista.append(item)
        else:
            hibak.append(item)
    osszegzes = sum(lista)
    return f"A megfelelően megadott értékek összege: {osszegzes}. A(z) {hibak} nem megfelelő beviteli érték."
    
print(osszegzes(1,2,"Felhő","Felhő2",1.2,3/4))




