
"""2. feladat____________________________________________________"""
import turtledemo.clock


def veletlenszam():
  import random
  szam=random.randint(1,100)
  print(szam)

#veletlenszam()

"""3. feladat_____________________________________________________"""
""" nem müxik"""
"""
def veletlen_datum_2025():

  start_date = datum(2025, 1, 1)
  end_date = datum(2025, 12, 31)

  time_between_dates = end_date - start_date
  days_between_dates = time_between_dates.days

  random_number_of_days = random.randrange(days_between_dates + 1)
  random_date = start_date + timedelta(days=random_number_of_days)

  print(random_date)


veletlen_datum_2025()
"""

"""4. feladat____________________________________________________"""

def veletlenlistaelem():
  import random
  names=["Alice","Bob","Charlie","Diana"]
  print(names)
  sorszam=random.randint(0,len(names)-1)
  print(sorszam)
  print(names[sorszam])

#veletlenlistaelem()

"""5. feladat____________________________________________________"""

from datetime import datetime

def idokulonbseg():
  kezdo_datum=input("kerem a kezdo datumot (YYYY-MM-DD formatumban): ")
  vegso_datum=input("kerem a vegso datumot (YYYY-MM-DD formatumban): ")
  try:
    kezdo_datum_obj = datetime.strptime(kezdo_datum,"%Y-%m-%d")
    vegso_datum_obj = datetime.strptime(vegso_datum,"%Y-%m-%d")
    napok=(vegso_datum_obj-kezdo_datum_obj).days
    print(f"A két dátum között {napok} nap van.")
  except ValueError:
    print("Hibás dátum formátum. Kérem YYYY-MM-DD formátumot használjon.")


#idokulonbseg()

"""6. feladat____________________________________________________"""

import random

def veletlen_szamsorozat():
  szamsorozat=[]
  for _ in range(10):
    szamsorozat.append(random.randint(1,50))
  print(szamsorozat)

#veletlen_szamsorozat()

"""7. feladat____________________________________________________"""
from datetime import datetime

def datum_ellenorzes():
  adott_datum = input("adj meg egy datumot, formatum: YYYY-MM-DD: ")
  try:
    datetime.strptime(adott_datum, "%Y-%m-%d")
    print("ervenyes datum, mert sikerult atkonvertalni")
    return True
  except ValueError:
    print("ervenytelen datum.")
    return False


datum_ellenorzes()