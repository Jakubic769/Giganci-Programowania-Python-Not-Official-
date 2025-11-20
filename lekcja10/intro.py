# chciałbym się przywitać w konsoli z każdym z Was
# print("Witaj Ignacy")
# print("Witaj Bartku")
# print("Witaj Livio")
# print("Witaj Mateuszu")
 
# def powitanie(lista_imion):
#     for imie in lista_imion:
#         print(f"Witaj {imie}!")
 
# powitanie(["Wiktorze", "Jakubie", "Mateuszu", "Malwino"])
 
def pitagoras(a, b, c, czy_wypisac=True):
    if a**2 + b**2 == c**2:
        if czy_wypisac:
            print("Trójkąt jest prostokątny")
        return True
    else:
        if czy_wypisac:
            print("Trójkąt jest nie prostokątny")
        return False
 
# pitagoras(12, 13, 5)
# pitagoras(b=12, c=13, a=5)
 
wynik1 = pitagoras(5, 12, c=13)
wynik2 = pitagoras(12, 5, c=13, czy_wypisac=True)
 
wynik3 = pitagoras(5, c=13, b=12, czy_wypisac=False)
print(wynik1, wynik2, wynik3)
 