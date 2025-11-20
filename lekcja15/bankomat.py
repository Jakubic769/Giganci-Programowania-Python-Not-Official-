import time

# Funkcja do sprawdzania poprawności karty i PIN-u
def logowanie(karty):
    karta = input("Podaj numer karty: ")
    if karta not in karty:
        print("Niepoprawny numer karty.")
        return None
    pin = input("Podaj PIN: ")
    if karty[karta]['pin'] == pin:
        print("Logowanie przebiegło pomyślnie.")
        return karta
    else:
        print("Niepoprawny PIN.")
        return None

# Funkcja do zmiany PIN-u
def zmiana_pin(karta, karty):
    nowy_pin = input("Podaj nowy PIN: ")
    karty[karta]['pin'] = nowy_pin
    print("PIN został zmieniony.")

# Funkcja do wypłaty gotówki
def wyplata(karta, karty):
    kwota = float(input("Podaj kwotę do wypłaty: "))
    if kwota <= karty[karta]['saldo']:
        karty[karta]['saldo'] -= kwota
        print(f"Wypłacono {kwota} PLN. Pozostałe saldo: {karty[karta]['saldo']} PLN.")
    else:
        print("Nie masz wystarczająco środków")

# Funkcja do wpłaty gotówki
def wplata(karta, karty):
    while True:
            kwota = float(input("Podaj kwotę do wpłaty: "))
            if kwota <= 0:
                print("Kwota musi być większa niż 0.")
            else:
                karty[karta]['saldo'] += kwota
                print(f"Wpłacono {kwota} PLN. Pozostałe saldo: {karty[karta]['saldo']} PLN.")
                break

# Funkcja do wyboru języka
def wybierz_jezyk():
    print("Wybierz język: ")
    print("1. Polski")
    print("2. Angielski")
    wybor = input("Podaj numer języka: ")
    return wybor

# Główna funkcja programu
def bankomat():
    # Baza danych kart
    karty = {
        "1234567890123456": {"pin": "1234", "saldo": 1000},
        "9876543210987654": {"pin": "5678", "saldo": 500},
    }

    # Wybór języka
    jezyk = wybierz_jezyk()
    if jezyk == "1":
        print("Witaj w bankomacie!")
    elif jezyk == "2":
        print("Welcome to the ATM!")
    else:
        print("Niepoprawny wybór języka.")
        return

    # Logowanie
    karta = logowanie(karty)
    if karta is None:
        return

    # Menu
    while True:
        print("\nWybierz opcję:")
        print("1. Sprawdź saldo")
        print("2. Wypłać gotówkę")
        print("3. Wpłać gotówkę")
        print("4. Zmień PIN")
        print("5. Zakończ")
        wybor = input("Podaj numer opcji: ")

        if wybor == "1":
            print(f"Twoje saldo wynosi: {karty[karta]['saldo']} PLN.")
        elif wybor == "2":
            wyplata(karta, karty)
        elif wybor == "3":
            wplata(karta, karty)
        elif wybor == "4":
            zmiana_pin(karta, karty)
        elif wybor == "5":
            print("Dziękujemy za korzystanie z bankomatu!")
            break
        else:
            print("Niepoprawny wybór.")

        time.sleep(1)

# Uruchomienie bankomatu
bankomat()
