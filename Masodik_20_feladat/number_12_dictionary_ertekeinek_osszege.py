# 12. Dictionary ertekeinek osszege
# Keszits egy fuggvenyt, amely visszaadja a dictionary ertekeinek az osszeget!
#
# Pelda input:
# d = {"a": 10, "b": 20, "c": 5}
# Elvart eredmeny:
# 35



d = {"a": 10, 
     "b": 20, 
     "c": 5
     }



def ertekek_osszege(d):
    a = d.values()
    return sum(a)


print(ertekek_osszege(d))