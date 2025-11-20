wyniki_konkursu = ["Marek", "Beata", "Karol", "Zuza", "Marta", "Roman"]
imie_uczestnika = input("Podaj swoje imie: ")
for i in range(len(wyniki_konkursu)):
    if imie_uczestnika == wyniki_konkursu[i]:
        print(f"Masz {i+1} miejsce!")