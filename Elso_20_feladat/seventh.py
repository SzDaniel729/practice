"""
### Listák és ciklusok
4. Írj egy programot, amely kiírja egy lista minden elemének a hosszát (pl. string lista).
5. Hozz létre egy listát 1-től 20-ig tartó számokkal, majd írd ki csak azokat a számokat, amelyek oszthatók 3-mal.
6. Készíts egy listát véletlenszerű számokkal, és add össze csak a páros számokat.

"""
#
# 4. Írj egy programot, amely kiírja egy lista minden elemének a hosszát (pl. string lista).
#

def lista_elemek_hozzaadasa(*args, **kwargs):
    local_list_int = []
    local_list_str = []
    local_list_else = []

    def lista_elemek_hossza_str():
            local_lista = []
            for item in local_list_str:
                local_lista.append(len(item))
            return local_lista
    
    def lista_elemek_hossza_int():
        return local_list_int
    

    def lista_elemek_hossza_else():
        return local_list_else
    
    def ertek():
        return {
            "A helyesen megadott stringek hossza": lista_elemek_hossza_str(),
            "Helytelenül megadott - számok - beviteli értékek": lista_elemek_hossza_int(),
            "Helytelenül megadott - egyéb típusú - beviteli értékek": lista_elemek_hossza_else()
        }

    for item in args:
        if isinstance(item, (int, float, complex)):
            local_list_int.append(item)
        elif isinstance(item, str):
            local_list_str.append(item)
        else:
            local_list_else.append(item)

    ertek_visszaadas_sortoressel = ertek ()
    for key, value in ertek_visszaadas_sortoressel.items():
        print(f"{key}: {value}")

lista_elemek_hozzaadasa("Alma", "Banán", 1, 2, 3,[1,2,3],{"1": 2})

######################################################################################################################################################################

#
# 5. Hozz létre egy listát 1-től 20-ig tartó számokkal, majd írd ki csak azokat a számokat, amelyek oszthatók 3-mal.
#

szamos_lista = []
for item in range(1, 21):
    szamos_lista.append(item)

def harommal_oszthato_szamok(*args):
    local_list = []
    for item in args:
        if item % 3 == 0:
            local_list.append(item)
    return local_list

print(harommal_oszthato_szamok(*szamos_lista))

######################################################################################################################################################################

#
# 6. Készíts egy listát véletlenszerű számokkal, és add össze csak a páros számokat.
#

random_lista = [13, 15, 30, 15, 79, 33, 99, 35, 9, 23, 37, 12, 11, 97, 55, 97, 61, 52, 20, 50, 40, 72, 17, 76, 76, 78]

def paros_szamok_osszeadasa():
    local_list = []
    for item in random_lista:
        if item % 2 == 0:
            local_list.append(item)
    return(sum(local_list))

print(paros_szamok_osszeadasa())




