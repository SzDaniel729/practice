# 8. Megszamlalas
# Irj egy fuggvenyt, amely megszamolja, hany darab szam van a listaban, ami nagyobb, mint 10!
#
# Pelda input:
# lista = [5, 15, 20, 8]
# Elvart eredmeny:
# 2

lista = [5, 15, 20, 8]

def nagyobb_mint_tiz(lista):
    local_list = []
    for item in lista:
        if 10 < item:
            local_list.append(item)
    return len(local_list)

print(nagyobb_mint_tiz(lista))