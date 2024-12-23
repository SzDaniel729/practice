# 10. Lista elemeinek szamolasa
# Keszits egy fuggvenyt, amely megszamolja, hany darab adott elem van a listaban!
#
# Pelda input:
# lista = [1, 2, 2, 3, 2, 4]
# elem = 2
# Elvart eredmeny:
# 3

lista = [1, 2, 2, 3, 2, 4]
elem = 2

def elemek_szama(lista, elem):
    local_list = []
    for item in lista:
        if elem == item:
            local_list.append(item)
    return len(local_list)

print(elemek_szama(lista, elem))
    