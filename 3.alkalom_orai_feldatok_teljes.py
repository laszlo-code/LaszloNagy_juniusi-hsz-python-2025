import math
"""

PI=3.14

MAX_POOL_CONNECTION=42
AGE_LIMIT=18

def test_age(age):
    if age<AGE_LIMIT:
        return False
    
response=test_age(17)
#FrontEnd (FE) -> halozaton -> False 
"""
"""
I. 
Feladat: Szorzat 
Egy függvényt tesztelünk, amely két szám szorzatát adja vissza eredményül. 
Írj egy függvényt "szorzat" néven, amely két számot vár paraméterül és visszaadja a 
szorzatukat. 
Ha nem számot adnak meg, fusson hibára!
"""

def szorzat():
  x=input("elso szam megadasa:")
  y=input("masodik szam megadasa:")
  try:
    x=int(x)
    y=int(y)
  except ValueError:
    print("HIBA. x vagy y nem szam!")
    return
  print("szorzat=",x+y)

szorzat()

"""
II. 
Feladat: Kisebb duplája 
Egy függvényt tesztelünk, amely két szám közül adja vissza a kisebb dupláját. 
Írj egy függvényt "kisebb_dupla" néven, amely két számot kap paraméterül és 
visszaadja a kisebb szám dupláját. 
"""

def kisebb_duplaja():
  print("ez a fuggveny a kisebb szam duplajat adja vissza")
  x=input("egyik szam:")
  y=input("masik szam:")
  if x<y:
    print("a kisebb szam duplaja:",int(x)*2)
  else:
    print("a kisebb szam duplaja:",int(y)*2)

kisebb_duplaja()

"""
III. 
Feladat: Páros vagy páratlan? 
Egy függvényt tesztelünk, amely egy egész szám alapján kiírja, hogy az páratlan
e. 
Írj egy függvényt "paros_paratlan" néven, amely a bejövő paraméter alapján kiírja, 
hogy az páros-e vagy páratlan. Pl. így: Ez a szám ... páros!
"""
def paros_vagy_paratlan():
  szam=input("adj meg egy szamot:")
  szam=int(szam)  #az input stringgel ter vissza, ezert at kell alakitani integerre
  print("a szam osztva 2-vel:",szam/2)
  if szam%2==0:
    print("ez egy paros szam, mert 2-vel maradek nelkül oszthato")
  else:
    print("ez a szam paratlan")

paros_vagy_paratlan()


"""
IV. Feladat: Nagyobb triplázva 
Egy függvényt tesztelünk, amely két szám közül adja vissza a nagyobb 
háromszorosát. 
Írj függvényt "nagyobbTripla" néven, amely visszaadja a két szám közül a nagyobb 
háromszorosát.
"""

def nagyobbtripla():
  szam1=input("egyik szam megadasa (szam1)")
  szam1=int(szam1)
  szam2=input("masik szam megadasa (szam2)")
  szam2=int(szam2)
  if szam1>szam2:
    print("szam1 a nagyob")
    print("szam1 haromszorosa:",szam1*3)
  else:
    print("szam2 a nagyob")
    print("szam2 haromszorosa:",szam2*3)

nagyobbtripla()