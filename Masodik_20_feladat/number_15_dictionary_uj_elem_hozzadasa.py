# 15. Uj elem hozzaadasa dictionary-hez
# Irj egy fuggvenyt, amely hozzaad egy uj kulcs-ertek part a dictionary-hez!
#
# Pelda input:
# d = {"a": 1, "b": 2}
# kulcs = "c"
# ertek = 3
# Elvart eredmeny:
# {"a": 1, "b": 2, "c": 3}

d = {"a": 1, 
     "b": 2
     }

kulcs = "c"
ertek = 3

def uj_elem(d, kulcs, ertek):
    d[kulcs] = ertek
    return d

print(uj_elem(d, "c", 3))
