# 3. Paros szamok szurese
# Irj egy fuggvenyt, amely visszaad egy uj listat a bemeneti listabol, csak a paros szamokkal!
#
# Pelda input:
# lista = [1, 2, 3, 4, 5, 6]
# Elvart eredmeny:
# [2, 4, 6]

lista = [1, 2, 3, 4, 5, 6]

def paros_szamok(lista):
    local_list = []
    for item in lista:
        if item % 2 == 0:
            local_list.append(item)
    return local_list

print(paros_szamok(lista))