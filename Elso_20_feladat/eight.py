"""
### Szótárak alapjai
7. Készíts egy szótárat, amely egy személy nevét és életkorát tartalmazza. Írd ki az életkorát.
8. Hozz létre egy szótárat az évszakokkal és a hozzájuk tartozó hónapokkal, majd kérd le belőle a nyári hónapokat.
9. Adj hozzá egy új kulcs-érték párost egy meglévő szótárhoz, majd törölj ki egy meglévő kulcsot.
"""


#
# 7. Készíts egy szótárat, amely egy személy nevét és életkorát tartalmazza. Írd ki az életkorát.
#

szemely = {
    "Név": "Nóra",
    "kor": 30
}


def kor():
    return szemely["kor"]

print(kor())


########################################################################################################################################################################

#
# 8. Hozz létre egy szótárat az évszakokkal és a hozzájuk tartozó hónapokkal, majd kérd le belőle a nyári hónapokat.
#

evszakok = {
    "Tavasz": ["Március", "Április", "Május"],
    "Nyár": ["Június","Július","Auguszts"],
    "Ősz": ["Szeptember","Október","November"],
    "Tél": ["December","Január","Február"]
}

nyari_honapok = evszakok["Nyár"]

print(nyari_honapok)

########################################################################################################################################################################

#
# 9. Adj hozzá egy új kulcs-érték párost egy meglévő szótárhoz, majd törölj ki egy meglévő kulcsot.
#

evszakok.update({"Napok": ["Hétfő","Kedd","Szerda","Csütörtök"]})

evszakok.pop("Tavasz")
print(evszakok)


