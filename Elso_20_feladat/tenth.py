"""
### If-else és logikai feltételek
13. Írj egy programot, amely bekér egy számot, és kiírja, hogy a szám pozitív, negatív vagy nulla.
14. Ellenőrizd, hogy egy adott lista tartalmaz-e egy konkrét elemet (pl. "alma").
15. Írj egy programot, amely bekér egy számot, és eldönti, hogy az páros vagy páratlan.
"""

#
# 13. Írj egy programot, amely bekér egy számot, és kiírja, hogy a szám pozitív, negatív vagy nulla.
#

def szam_ertek(*args):
    local_lista_szamok = []
    local_lista_hiba = []
    
    def szam_e():
        for item in args:
            if isinstance(item, (int,float,complex)):
                local_lista_szamok.append(item)
            else:
                local_lista_hiba.append(item)

    def beviteli_ertek():
        eredmeny = []
        for item in local_lista_szamok:
            if item > 0:
                eredmeny.append(f"A(z) {item} pozitív.")
            elif item < 0:
                eredmeny.append(f"A(z) {item} negatív.")
            else:
                eredmeny.append(f"A(z) {item} nulla.")
        return eredmeny
    
    szam_e()
    return beviteli_ertek()

print(szam_ertek(1,2,0,-1,1.2,3/4,"alma"))
            
######################################################################################################################################################################

#
# 14. Ellenőrizd, hogy egy adott lista tartalmaz-e egy konkrét elemet (pl. "alma").
#

random_lista = [63, 94, 'körte', 17, 16, 86, 33, 'barack', 1, 'barack', 56, 14, 7, 22, 'barack', 82, 'szilva', 'barack', 23, 23, 'körte', 86, 28, 'szilva', 60, 'szilva', 73, 'barack', 68, 'barack', 72, 'körte', 'barack', 5, 'szilva', 'alma', 'alma', 37, 'körte', 35, 'szilva', 'körte', 'alma', 4, 13, 0, 'barack', 93, 'körte', 'szilva', 44, 'szilva', 'barack', 68, 'barack', 38, 73, 34, 'alma', 'szilva', 'körte', 'barack', 'szilva', 24, 'barack', 89, 'körte', 'barack', 'szilva', 72, 0, 79, 'körte', 31, 'körte', 'körte', 'körte', 'szilva', 'körte', 'szilva', 'körte', 53, 22, 47, 55, 54, 12, 34, 7, 82, 18, 99, 65, 43, 'körte', 'barack', 24, 'körte', 'barack', 'alma']

def alma_kereses():
    local_lista = []
    for item in random_lista:
        if item == "alma":
            local_lista.append(item)
        else:
            pass
    print(len(local_lista))

alma_kereses()
                
######################################################################################################################################################################

#
# 15. Írj egy programot, amely bekér egy számot, és eldönti, hogy az páros vagy páratlan.
#

def paros_paratlan(num1):
    if num1 % 2 == 0:
        return f"A(z) {num1} páros szám."
    else:
        return f"A(z) {num1} páratlan szám."
    
print(paros_paratlan(4))
















