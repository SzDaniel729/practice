"""
### If-else és komplexebb logika
16. Készíts egy programot, amely bekér egy jelszót, és ellenőrzi, hogy az legalább 8 karakter hosszú és tartalmaz-e számot.
17. Írj egy programot, amely bekér két számot, és eldönti, hogy az első osztható-e a másodikkal.
18. Írj egy programot, amely bekér egy évet, és eldönti, hogy az szökőév-e.
"""

#
# 16. Készíts egy programot, amely bekér egy jelszót, és ellenőrzi, hogy az legalább 8 karakter hosszú és tartalmaz-e számot.
#

def jelszo_bekeres(jelszo):
    
    def jelszo_hosszusag_ellenorzes():
        if len(jelszo) < 8:
            return "A megadott jelszóban minimum 8 karakternek kell lennie."

    def jelszo_szam_ellenorzes():
        if not any(char.isdigit() for char in jelszo):
            return "A jelszónak tartalmaznia kell legalább egy számot."
        
    return jelszo_hosszusag_ellenorzes() or jelszo_szam_ellenorzes()


print(jelszo_bekeres("aasdasdasdwas1"))

############################################################################################################################################

#
# 17. Írj egy programot, amely bekér két számot, és eldönti, hogy az első osztható-e a másodikkal.
#

def oszthatosag(num1, num2):
    if num1 % num2 == 0:
        return f"A(z) {num1} osztható a(z) {num2}"
    else:
        return f"A(z) {num1} nem osztható a(z) {num2}"

print(oszthatosag(2,1))

#
# 18. Írj egy programot, amely bekér egy évet, és eldönti, hogy az szökőév-e.
#

def szokoev_e(num):
    if num % 4 == 0:
        return f"A(z) {num} szökőév"
    else:
        return f"A(z) {num} nem szökőév"


print(szokoev_e(1001))




