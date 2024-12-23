# 9. Lista elemeinek kivonasa
# Irj egy fuggvenyt, amely egy listabol minden szamot kivon egy adott szambol!
#
# Pelda input:
# lista = [1, 2, 3]
# szam = 10
# Elvart eredmeny:
# [9, 8, 7]

lista = [1, 2, 3]
szam = 10

def kivonas(lista, szam):
    local_list = []
    for item in lista:
        local_list.append(10-item)
    return local_list

print(kivonas(lista, 10))