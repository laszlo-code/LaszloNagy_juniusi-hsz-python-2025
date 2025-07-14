import random
import statistics


szam_lista = [random.randint(1, 100) for _ in range(10)]
print("veletlen szam lista:", szam_lista)


szerencseszam = random.choice(szam_lista)
print("szerencseszam:", szerencseszam)


atlag = statistics.mean(szam_lista)
szoras = statistics.stdev(szam_lista)
maximum = max(szam_lista)
minimum = min(szam_lista)
osszeg = sum(szam_lista)
osszeg_gyoke = osszeg**0.5

print("atlag:", atlag)
print("szoras:", szoras)
print("maximum:", maximum)
print("minimum:", minimum)
print("osszeg:", osszeg)
print("osszeg gyoke", osszeg_gyoke)


def is_prime(szerencseszam):
    if szerencseszam <= 1:
        return False
    for i in range(2, int(szerencseszam**0.5) + 1):
        if szerencseszam % i == 0:
            return False
    return True

if is_prime(szerencseszam):
    print(f"a szerencseszam {szerencseszam} primszam!")
else:
    print(f"szerencseszam {szerencseszam} nem primszam.")



from datetime import date

today = date.today()
print("mai datum", today)
print("a het napja", today.strftime("%A"))
print("az ev napja:", today.timetuple().tm_yday)

"""_______________________________________________________________________"""

import datetime

szulinap_str = input("vizsgalt szulinap (honap.nap?): ")
honap, nap = map(int, szulinap_str.split('.'))

now = datetime.date.today()
try:
    szulinap_datum = datetime.date(now.year, honap, nap)
except ValueError:
    print("hibas datum megadas.")
    exit()


if szulinap_datum < now:
    szulinap_datum = datetime.date(now.year + 1, honap, nap)

hatralevo_napok = szulinap_datum - now
print(f"hatralevo napok addig {hatralevo_napok.days}")

"""_____________________________________________________________________________"""

import math
import random

vizsgalt_szog=random.uniform(0,360)
print("A vizsgalt szog "+str(vizsgalt_szog)+" fok.")
muvelet=input("sin vagy cos valasztas: ")
tipp_str=input("szerinted mennyi? : ")

try:
    tipp = float(tipp_str)
except ValueError:
    print("hibas bevitel, szamot adj meg.")
    exit()


if muvelet=="sin":
  eredmeny=math.sin(math.radians(vizsgalt_szog))
elif muvelet=="cos":
  eredmeny=math.cos(math.radians(vizsgalt_szog))
else:
    print(" !sin' vagy 'cos' adj meg.")
    exit()


print("a helyes valasz: ", eredmeny)
if tipp > 0.9 * eredmeny and tipp < 1.1 * eredmeny:
  print("jo, kevesebb mint 10% elteres")
else:
  print("rossz valasz")


  """_________________________________________________________________"""
import math
import datetime
import random

veletlen_idopont1=random.datetime
