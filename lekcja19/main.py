from uzytkownicy import Uzytkownik
from uzytkownicy import Przywitanie

# user1 = Uzytkownik()
# print(user1)
# print(user1.imie)
# print(user1.nick)
# print(user1.wiek)

# user1.imie = "Wasyl"
# user1.nick = "Aragorn"
# user1.wiek = 25

# print(user1.imie)
# print(user1.nick)
# print(user1.wiek)

# user2 = Uzytkownik()

# user2.imie = "Balbina"
# user2.nick = "Szczur Pasiasty"
# user2.wiek = 5

# print(user2.imie)
# print(user2.nick)
# print(user2.wiek)

user3 = Uzytkownik(imie="Jakub",
                   nick="Puchatek",
                   wiek=13)

print(user3.imie)
print(user3.nick)
print(user3.wiek)

Przywitac_sie = Przywitanie(imie="Jakub",   
                            nick="Puchatek",
                            wiek=13)

print(Przywitanie)