# 14. Dictionary kulcs szerinti keresese
# Keszits egy fuggvenyt, amely visszaadja egy adott kulcshoz tartozo erteket a dictionary-bol!
#
# Pelda input:
# d = {"a": 10, "b": 20}
# kulcs = "a"
# Elvart eredmeny:
# 10

d = {"a": 10, 
     "b": 20
     }

kulcs = "a"

def keres_kulcs(d: dict, kulcs):
    for key, value in d.items():
        if key == kulcs:
            return value
        


print(keres_kulcs(d, kulcs))