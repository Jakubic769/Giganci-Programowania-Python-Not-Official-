pusty_slownik = {}
pusta_lista = []

slownik = {"A": "Andersen",
           "B": ["Bogusz", "Boros"]}

uzytkownicy = {
    2348767: {"login": "Wiktor", "hasło": "sdifg72g7c"},
    2837562: {"login": "Aga", "hasło": "dsfgherth"},
}

# dla słowników mamy 3 metody:
# słownik.keys() -> zwraca nam listę wszystkich kluczy,
# słownik.values() -> zwraca nam listę wszystkich wartości,
# słownik.items() -> zwraca nam dwie listy, kluczy i wartości

for id_uzytkownika, dane_uzytkownika in uzytkownicy.items():
    print(id_uzytkownika)
    print(dane_uzytkownika["login"])
    
for id_uzytkownika in uzytkownicy.keys():
    print(id_uzytkownika)
    
for dane_uzytkownika in uzytkownicy.values():
    print(dane_uzytkownika)