# 7. Lista megforditasa
# Keszits egy fuggvenyt, amely megforditja a listat!
#
# Pelda input:
# lista = [1, 2, 3, 4]
# Elvart eredmeny:
# [4, 3, 2, 1]

lista = [1, 2, 3, 4]

def megforditas(lista):
    return lista[::-1]

print(megforditas(lista))