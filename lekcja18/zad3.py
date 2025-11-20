import random

x = input("Orzeł (o) czy Reszka (r)? (lub wpisz 'q', aby zakończyć): ").lower()

gracz = 0
komputer = 0

def rzut():
    return random.choice(["o", "r"])

while x != "q":  
    if x not in ["o", "r"]:
        print("Nieprawidłowy wybór! Wybierz 'o' (Orzeł) lub 'r' (Reszka).")
    else:
        wynik_rzutu = rzut()
        print(f"Wynik rzutu: {'Orzeł' if wynik_rzutu == 'o' else 'Reszka'}")
        if x == wynik_rzutu:
            print("Wygrałeś!")
            gracz += 1
        else:
            print("Przegrałeś!")
            komputer += 1
    

    print(f"Wynik gracza: {gracz} | Wynik komputera: {komputer}")
    
    x = input("Orzeł (o) czy Reszka (r)? (lub wpisz 'q', aby zakończyć): ").lower()

print("Dzięki za grę!")
