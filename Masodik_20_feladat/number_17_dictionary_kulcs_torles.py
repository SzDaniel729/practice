# 17. Kulcs torlese a dictionary-bol
# Irj egy fuggvenyt, amely torol egy megadott kulcsot a dictionary-bol!
#
# Pelda input:
# d = {"a": 1, "b": 2, "c": 3}
# kulcs = "b"
# Elvart eredmeny:
# {"a": 1, "c": 3}

d = {"a": 1, 
     "b": 2, 
     "c": 3
     }

kulcs = "b"

def kulcs_torlese(d: dict, kulcs):
    d.pop(kulcs)
    return d

print(kulcs_torlese(d, kulcs))



