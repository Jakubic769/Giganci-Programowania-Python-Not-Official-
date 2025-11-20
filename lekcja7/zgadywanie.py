import random
 
MAX = 100
MIN = 0
 
niewiadoma = random.randint(MIN, MAX)
strzal = int(input(f"Proszę zgadnij liczbę od {MIN} do {MAX}: "))
while niewiadoma != strzal:
    odleglosc = niewiadoma - strzal
    odleglosc = abs(odleglosc)
    if strzal > 100:
        continue
    if 50 <= odleglosc < 100:
        print("Bardzo zimno")
    elif 10 <= odleglosc < 50:
        print("Cieplej")
    elif 1 <= odleglosc < 10:
        print("Bardzo ciepło")
    else:
        print("Gorąco!!!")
    input_uzytkownika = input(f"Proszę zgadnij liczbę od {MIN} do {MAX}: ")
    if input_uzytkownika == "q":
        print("Dzięki za grę, powodzenia następnym razem!")
        break
    elif input_uzytkownika == "p":
        print(f"Poprawna odpowiedż to: {niewiadoma}")
        continue
    strzal = int(input_uzytkownika)
 