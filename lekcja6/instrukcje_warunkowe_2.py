poprawne_haslo = "1111"
pin = "2222"
haslo_uzytkownika = input("Podaj hasło: ")
if poprawne_haslo == haslo_uzytkownika:
    pin_uzytkownika = input("Podaj Pin: ")
    if pin == pin_uzytkownika:
        print("Logowanie poprawne")
    else:
        print("Podałes niepoprawny PIN")
else:
    print("Nie udało się zalogować") 
    