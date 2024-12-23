# 11. Dictionary kulcsainak szama
# Irj egy fuggvenyt, amely visszaadja egy dictionary kulcsainak a szamat!
#
# Pelda input:
# d = {"a": 1, "b": 2, "c": 3}
# Elvart eredmeny:
# 3


d = {
    "a": 1, 
    "b": 2, 
    "c": 3
    }



def kulcsok_szama(d):
    return len(d)

print(kulcsok_szama(d))
