"""### Szótárak és ciklusok
10. Írj egy programot, amely kiírja egy szótár minden kulcsát és értékét soronként.
11. Hozz létre egy szótárat, ahol a kulcsok nevek, az értékek pontszámok (pl. dolgozat eredményei). Számold ki az átlagos pontszámot.
12. Írj egy programot, amely összehasonlít két szótárat, és kiírja a közös kulcsokat.
"""

#
# 10. Írj egy programot, amely kiírja egy szótár minden kulcsát és értékét soronként.
#

pelda = {
    "szín": "Fekete",
    "típus": "kocka",
    "Kiadvány": 25,
    "Szolgáltatások": 11,
    "Ablak": "Ablak",
    "József": 23,
    "Csaba": 13
}

def sor_kiiras():

    for key, value in pelda.items():
        print(f"{key}: {value}")

sor_kiiras()


########################################################################################################################################################################

#
# 11. Hozz létre egy szótárat, ahol a kulcsok nevek, az értékek pontszámok (pl. dolgozat eredményei). Számold ki az átlagos pontszámot.
#

pelda2 = {
    "Béla": 18,
    "Dani": 20,
    "Feri": 25,
    "Isvtán": 11,
    "Péter": 15,
    "József": 23,
    "Csaba": 13
}

def atlag_pontszam():
    local_lista= []
    for key, value in pelda2.items():
        local_lista.append(value)
    print(sum(local_lista))

atlag_pontszam()

########################################################################################################################################################################

#
# 12. Írj egy programot, amely összehasonlít két szótárat, és kiírja a közös kulcsokat.
#

def szotarak_osszehasonlitasa():
    elso_szotar_kulcsai = []
    masodik_szotar_kulcsai = []
    elso_szotar_kulcsai.extend(pelda.keys())
    masodik_szotar_kulcsai.extend(pelda2.keys())

    kozos_ertekek = []
    for key1, key2 in zip(elso_szotar_kulcsai, masodik_szotar_kulcsai):
        if key1 == key2:
            kozos_ertekek.append(key1)
    print(kozos_ertekek)

szotarak_osszehasonlitasa()










