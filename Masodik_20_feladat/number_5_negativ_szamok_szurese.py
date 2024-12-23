# 5. Negativ szamok szurese
# Irj egy fuggvenyt, amely visszaad egy listat, amiben csak a negativ szamok szerepelnek a bemeneti listabol!
#
# Pelda input:
# lista = [-1, 2, -3, 4, -5]
# Elvart eredmeny:
# [-1, -3, -5]

lista = [-1, 2, -3, 4, -5]

def negativ_szamok(lista):
    local_list = []
    for item in lista:
        if item < 0:
            local_list.append(item)
    return local_list

print(negativ_szamok(lista))