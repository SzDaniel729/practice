# 18. Dictionary atlag erteke
# Keszits egy fuggvenyt, amely visszaadja a dictionary ertekeinek atlagat!
#
# Pelda input:
# d = {"a": 10, "b": 20, "c": 30}
# Elvart eredmeny:
# 20.0

d = {"a": 10, 
     "b": 20, 
     "c": 30
     }

def ertekek_atlaga(d: dict):
    ossz = sum(d.values())
    ertekek = len(d)
    atlag = ossz / ertekek
    return atlag

print(ertekek_atlaga(d))