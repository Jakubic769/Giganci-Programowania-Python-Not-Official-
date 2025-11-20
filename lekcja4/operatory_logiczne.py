import time

#input() -> zwraca domyślnie str

#nie wiem co zrobic!

cena_bananow = 4.79

czy_sklep_otwarty = True
produkt_dostepny = True

print("Właśnie planujesz kupić banany!")
time.sleep(2)
kasa = float(input("Podaj ile masz kasy?\n"))
ile_bananow_chce_kupic = float(input("Podaj ile kilogramów tych bananów chcesz kupić?\n"))

koszt = ile_bananow_chce_kupic * cena_bananow
czy_cie_stac = kasa >= koszt

print(f"Czy możesz kupić banany?: {czy_cie_stac and czy_sklep_otwarty and produkt_dostepny}")

# not
# and
# or

# przykład not
###jest_wieczor = True
###nie_jest_wieczor = not jest_wieczor
###print(jest_wieczor)
###print(nie_jest_wieczor)

# przykład and

###dostepnosc_produktu = True
###wystarczajaca_kasa = True

###print(f"Czy mogę kupić te banany? {dostepnosc_produktu and wystarczajaca_kasa}")

# przykład or

###wystarczajaca_gotowka = False
###wystarczajaca_kasa_na_koncie = False

###print(f"Czy mogę kupić te banany? {wystarczajaca_gotowka and wystarczajaca_kasa_na_koncie}")

# bardziej złożone wyrażenie

#banany_dostepne = True
#wystarczajaca_gotowka = False
#wystarczajaca_kasa_na_koncie = True

#print(f"Czy mogę kupić te banany? {banany_dostepne and wystarczajaca_gotowka or banany_dostepne and wystarczajaca_kasa_na_koncie}")

#not jest pierwszy, potem and, potem or