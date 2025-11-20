liczba_biletow = int(input("Ile biletów chcesz zakupić: "))
cena_biletu = 0

while cena_biletu == 0:
    miesiac = int(input("Podaj miesiąc, w jakim planujesz sie do nas wybrać: "))
    if miesiac == 1 or miesiac == 2 or miesiac == 12:
        cena_biletu = 50
    elif miesiac == 3 or miesiac == 4 or miesiac == 10 or miesiac == 11:
        cena_biletu = 100
    elif miesiac == 5 or miesiac == 6 or miesiac == 8 or miesiac == 9:
        cena_biletu = 200
    elif miesiac == 7:
        cena_biletu = 250
    else:
        print("Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie")
print(f"Cena biletów: {cena_biletu*liczba_biletow}")