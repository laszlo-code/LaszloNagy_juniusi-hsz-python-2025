"""
1. Magánhangzó-számláló
Kérj be egy szöveget, és számold meg, hány magánhangzót tartalmaz!
(A, E, I, O, Ö, U, Ü + kisbetűk is)
Példa:
Bemenet: Hello Világ
Kimenet: 4 magánhangzó található.
"""
maganhangzok=['A','Á','E','É','I','Í','O','Ó','Ö','Ő','U','Ú','Ü','Ű','a','á','e','é','i','í','o','ó','ö','ő','u','ú','ü','ű']
print("magyar maganhangzok listaja:",maganhangzok)
szoveg=input("Kérem a szöveget:")
print("megadott szoveg:",szoveg)
szamlalo=0
for betu in szoveg:
    if betu in maganhangzok:
        szamlalo+=1
print(f"{szamlalo} magyar magánhangzó található.")
"""
__________________________________________________________
"""
"""
2. Számjegyek összege
Kérj be egy egész számot, majd számold össze a számjegyeit!
Pl. 753 → 7 + 5 + 3 = 15
Tipp: alakítsd át stringgé, menj végig rajta, és alakítsd vissza az egyes karaktereket int()-tel.
"""
szam_str = input("kerek egy egesz szamot: ")
print("a megadott szam:", szam_str)

osszeg = 0
for jegy in szam_str:
    osszeg += int(jegy)

print("A számjegyek összege:", osszeg)

"""
___________________________________________________________________
"""

"""
3. Szavak visszafelé
Kérj be egy mondatot, és írd ki a szavait visszafelé sorrendben, de a szavak betűit ne fordítsd
meg!
Példa:
Bemenet: Szeretem a Python nyelvet
Kimenet: nyelvet Python a Szeretem
Tipp: split(), majd reversed() vagy [::-1]
"""

mondat = input("irj egy mondatot: ")
print("eredeti mondat:", mondat)

szavaklistaja = mondat.split()
print("szavak listaja:", szavaklistaja)

szavaklistaja.reverse()
print("szavak forditott listaja, reverse metodus utan-:", szavaklistaja)
print("valtozo tipusa",type(szavaklistaja))

visszafele_mondat = " ".join(szavaklistaja)

print("szavak visszafelé (itt mar joinolas utan):", visszafele_mondat)
print("ez milyen tipusu valtozo:",(type(visszafele_mondat)))

"""
__________________________________________________________________________
"""

"""
4. Leggyakoribb szám
Kérj be számokat egy listába (Enterrel lezárható), majd írd ki, melyik szám szerepelt a
legtöbbször, és hányszor!
Tipp: Olyan, mint a feladatok_pontok(), de itt a leggyakoribb értéket keresed.
"""


szamok_listaja = []
be=input("Kérem a számokat: (ket szam között:Enter, bevitel befejezese: nincs szam + enter) ")
while  be!="":

    szamok_listaja.append(int(be))
    be=input("Kérem a számot: (+Enter) ")
print("Megadott számok listája:", szamok_listaja)

lista_hossza = len(szamok_listaja)
print("szamsor elemeinek szama:", lista_hossza)

pass
print("EZ NINCS BEFEJEZVE")

"""
____________________________________________________________
"""

"""
5. Egyszerű jelszó-ellenőrző
Írj egy függvényt, ami bekér egy jelszót, és eldönti, hogy elég erős-e!
A jelszó akkor erős, ha:
 Legalább 8 karakter hosszú
 Tartalmaz számot
 Tartalmaz nagybetűt
 Tartalmaz kisbetűt
Tipp: használhatsz any(c.isdigit() for c in jelszo) jellegű megoldást.
"""


def jelszo_ellenorzo(jelszo):
    if len(jelszo) < 8:
        return False
        # a jelszo tul rövid, 8 vagy tobb karakter

    if not any(c.isdigit() for c in jelszo):
        return False
        # legalabb 1 szam legyen benne

    if not any(c.isupper() for c in jelszo):
        return False
        # legalabb 1 nagybetu kell

    if not any(c.islower() for c in jelszo):
        return False
    # legalabb 1 kisbetu kell

    return True  # ha nincs hiba, vagyis van benne minden ami kell


bekert_jelszo = input("Kérek egy jelszót: ")

if jelszo_ellenorzo(bekert_jelszo):
    print("A jelszó erős.")
else:
    print("A jelszó nem elég erős.")