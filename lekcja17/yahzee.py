"""

1. Rzucanie kośćmi
2. Przerzucanie kości
3. Zapisywanie rezultatów
4. Stworzenie górnej tabeli.
5. Stworzenie dolnej tabeli.

"""

import random 

wynik_rzutu = [1, 2, 3, 4, 5]
nazwy_punktow = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątki", "Szóstki"]
punkty = ["", "", "", "", "", ""]
# punktacja = {"Jedynki": "", ..., "Szóstki": ""}

def pokaz_tabele_punktow():
    print("_________________")
    for i in range(len(punkty)):
        print(f"{i+1}.{nazwy_punktow[i]}\t{punkty[i]}")
    print("_________________")
    
def wstaw_punkty():
    pole = int(input("Gdzie chcesz wpisać swój wynik rzutu: "))
    oblicz_wynik(pole)
    
def oblicz_wynik(liczba: int):
    liczba_punktow = 0
    for wynik in wynik_rzutu:
        print(f"Wynik rzutu kością: {wynik}")
        if wynik == liczba:
            print("Odnaleziono taki sam wynik")
            liczba_punktow += liczba
            print(f"Nowa suma punktów to: {liczba_punktow}")
    index = liczba -1
    punkty[index] = liczba_punktow

def rzuc_koscmi(indexy_kosci: str="01234"):
    for numer in indexy_kosci:
        # print(f"Odczytany numer indexu który chcę przerzucić to: {numer}")
        index = int(numer)
        # print(f"Poprzednia wartość na indexie {index} wynosi {wynik_rzutu[index]}")
        wynik_rzutu[index] = random.randint(1, 6)
        # print(f"Nowa wartość na indexie {index} wynosi {wynik_rzutu[index]}")     


rzuc_koscmi()
pokaz_tabele_punktow()
for tura in range(10):
    for i in range(2):
        print(wynik_rzutu)
        przerzuty = input("Podaj jakie kości chcesz przerzucić, wpisz q aby zakończyć turę: ")
        if przerzuty == "q":
            break
        else:
            rzuc_koscmi(przerzuty)
    print(wynik_rzutu)
    wstaw_punkty()
    pokaz_tabele_punktow()
print(f"Gra się zakończyła. Suma punktów użytkownika wynosi: {sum(punkty)}")


# 1 TO 0
# 2 TO 1
# 3 TO 2
# 4 TO 3
# 5 TO 4
                 
























                 