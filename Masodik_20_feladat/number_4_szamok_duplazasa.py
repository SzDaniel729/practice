# 4. Szamok duplazasa
# Keszits egy fuggvenyt, amely visszaad egy uj listat, ahol minden szam duplazva van!
#
# Pelda input:
# lista = [1, 2, 3]
# Elvart eredmeny:
# [2, 4, 6]

lista = [1, 2, 3]

def duplazas(lista):
    local_list = []
    for item in lista:
        local_list.append(item*2)
    return local_list

print(duplazas(lista))

