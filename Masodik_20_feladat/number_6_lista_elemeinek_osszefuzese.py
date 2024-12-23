# 6. Lista elemeinek osszefuzese
# Irj egy fuggvenyt, amely osszefuz egy listaban levo szovegeket egyetlen szovegge!
#
# Pelda input:
# lista = ["hello", "world"]
# Elvart eredmeny:
# "helloworld"

lista = ["hello", "world"]

def osszefuz(lista):
    fuzes = " ".join(map(str,lista))
    return fuzes

print(osszefuz(lista))