# 13. Dictionary ertekeinek duplazasa
# Irj egy fuggvenyt, amely megduplazza a dictionary ertekeit!
#
# Pelda input:
# d = {"a": 1, "b": 2}
# Elvart eredmeny:
# {"a": 2, "b": 4}

d = {"a": 1,
      "b": 2
      }

def ertekek_duplazasa(d: dict):
    for values in d:
        d[values] *= 2

ertekek_duplazasa(d)

print(d)
