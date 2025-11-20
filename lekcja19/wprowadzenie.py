# chciałbym abyście utworzyli konta 4 użytkowników. Musimy zapisać takie informacje jak:
# imie
# nick
# wiek

# napiszcie do tego funkcję, która przywita się z użytkownikiem:
def przywitanie(imie, nick, wiek):
    print(f"Witaj {imie}, twój nick to {nick}. Masz {wiek} lat.")
    


imie2 = "Jakub"
nick2 = "Makaron"
wiek2 = 14

imie3 = "Robert"
nick3 = "Akita"
wiek3 = 14

imie4 = "Livia"
nick4 = "Demonkot"
wiek4 = 14

przywitanie(imie1, nick1, wiek1)

przywitanie(imie2, nick2, wiek2)

przywitanie(imie3, nick3, wiek3)

przywitanie(imie4, nick4, wiek4)

users = {
    1: {
        "imie": "Agnieszka",
        "nick": "Filemon",
        "wiek": 14
    },
}
