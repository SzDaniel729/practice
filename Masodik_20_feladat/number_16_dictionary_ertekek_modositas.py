# 16. Dictionary ertekek modositas
# Keszits egy fuggvenyt, amely megszorozza az osszes erteket egy adott szammal!
#
# Pelda input:
# d = {"a": 2, "b": 3}
# szam = 3
# Elvart eredmeny:
# {"a": 6, "b": 9}

d = {"a": 2, 
     "b": 3
     }

def ertekek_szorzasa(d, szam):
    for values in d:
        d[values] *= szam
    return d

print(ertekek_szorzasa(d, 3))

