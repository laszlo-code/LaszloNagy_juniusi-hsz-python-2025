#szokoev

ev=input("melyik evet vizsgaljuk: ?")
ev=int(ev)
if ev%400==0:
  print("szokoev")
elif ev%100==0:
  print("nem szokoev")
elif ev%4==0:
  print("szokoev")
else:
    print("nem szokoev")

#__________________________________________________
#szamsor elemeinek atlaga

szamok = [24, 31, 22, 43, 10, 84, 38, 44, 84, 56, 67, 51, 56, 84, 31, 65,
            69, 83, 39]
szum = 0
db = len(szamok)

def atlag_szamitas():
      global szum
      for x in szamok:
          szum += x
      global atlag
      atlag = szum / db

szurt = []

def szurt_list():
      global atlag
      for x in szamok:
          if x < atlag:
              szurt.append(x)


atlag_szamitas()
szurt_list()

print("elemek atlaga:", atlag)
print("atlagnal kisebb szamok:", szurt)

#__________________________________________________
# betucsere



szo=input("mi legyen a szo?")
hanyadik=input("hanyadik betut csereljük le?")
mirecsere=input("mire csereljük le? (helyettesito betu)")

szo=str(szo)
hanyadik=int(hanyadik)
mirecsere=str(mirecsere)
pozicio=hanyadik-1

lecserelendo_betu=szo[pozicio]
print("ezt a betut csereljuk le:", lecserelendo_betu)

print(szo.replace)(lecserelendo_betu,mirecsere)

uj_szo = szo.replace(lecserelendo_betu,mirecsere)
print(uj_szo)

# ez a betucsere feladat nincs tokeletesen megoldva
