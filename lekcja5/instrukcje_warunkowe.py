import time

cena_bananow = 6.99
cena_bananow_premium = 9.99

czy_sklep_otwarty = True
banany_dostepny = True
banany_premium_dostepny = True

# input() -> zwraca domyślnie str
print("Właśnie planujesz kupić banany!")
time.sleep(1)
czy_chce_banany_zwykle = "tak" == (input("Czy chcesz zakupić banany zwykłe?"))
czy_chce_banany_premium = "tak" == (input("Czy chcesz zakupić banany premium?"))

cena_produktow = 0

if czy_chce_banany_zwykle == True:
    kg_bananow = float(input("Ile kilogramów bananów chcesz zakupić?"))
    cena_produktow += round(kg_bananow*cena_bananow, 2)
if czy_chce_banany_premium == True:
    kg_bananow_premium = float(input("Ile kilogramów bananów Premium chcesz zakupić?"))
    cena_produktow += round(kg_bananow_premium*cena_bananow_premium, 2)
ilosc_pieniedzy = float(input("Ile posiadasz pieniędzy. Jeśli masz aplikacje będzie mniej kosztować!"))
czy_korzystasz_z_karty_sklepu = "tak" == (input("Czy korzystasz z karty sklepu?"))
if czy_korzystasz_z_karty_sklepu == True:
    float(cena_produktow) - (25/10)
    

czy_klienta_stac = ilosc_pieniedzy >= cena_produktow

czy_kupisz = czy_klienta_stac and banany_dostepny and czy_sklep_otwarty
if (czy_kupisz == True):
    print("Masz wystarczającej ilości pieniędzy.")
    time.sleep(1)
    print("Dziękuje za zakupy!")
else:
    if czy_klienta_stac == False:
        print("Masz za mało pieniędzy")
    if czy_sklep_otwarty == False:
        print("Niestety, jesteśmy już zamknięci")

