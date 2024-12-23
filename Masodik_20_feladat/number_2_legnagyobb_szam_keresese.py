# 2. Legnagyobb szam megkeresese
# Keszits egy fuggvenyt, amely visszaadja a listaban levo legnagyobb szamot!
#
# Pelda input:
# lista = [10, 20, 5, 8, 30]
# Elvart eredmeny:
# 30

lista = [10, 20, 5, 8, 30]

def legnagyobb_szam(lista):
    local_value = 0
    for item in lista:
        if item > local_value:
            local_value = item
    return local_value

print(legnagyobb_szam(lista))