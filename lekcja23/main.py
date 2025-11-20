from random import randint, choice
from time import sleep

class Postac:
    def __init__(self):
        self.nazwa = ""
        self.zycie = 1
        self.max_zycie = 1
    
    def atakuj(self, przeciwnik):
        atak = randint(0, 3)
        if(atak == 0):
            print(f"{przeciwnik.nazwa} unika ataku")
        else:
            print(f"{self.nazwa} atakuje {przeciwnik.nazwa}, zadając {atak} obrażeń")
            przeciwnik.zycie-=atak


class Przeciwnik(Postac):
    def __init__(self, gracz):
        super().__init__()
        self.nazwa = choice(['szkielet', 'zombie', 'wampir'])
        self.zycie = randint(1, gracz.max_zycie)

class Gracz(Postac):
    def __init__(self):
        super().__init__()
        self.zycie = 10
        self.max_zycie = 10
        self.nazwa = input("Wpisz swój nickname: ")

    def odpoczynek(self):
        self.zycie += 1
        sleep(1)
        if(self.zycie > self.max_zycie):
            self.zycie = self.max_zycie
        print(f"{self.nazwa} odpoczywa... Aktualne życie: {self.zycie}/{self.max_zycie}")

    def walka(self, Przeciwnik):
        walka = True
        while walka:
            print(f"życie {Przeciwnik.nazwa}: {Przeciwnik.zycie}")
            akcja = input("Wybierz akcję [atakuj/uciekaj]:")

            if akcja == "atakuj":
                self.atakuj(Przeciwnik)
                if Przeciwnik.zycie <= 0:
                    print("Wygrałeś!")
                    return True
                Przeciwnik.atakuj(self)
            elif akcja == "uciekaj":
                print(f"{self.nazwa} ucieka")
                Przeciwnik.atakuj(self)
                walka = False
            else:
                print("akcja nieznana")
            
            if self.zycie <= 0:
                print("Przegrałeś!")
                return False
        return True

gracz = Gracz()
gra = True
while gra:
    akcja = input("Wybierz akcję [zwiedzaj, odpocznij]: ")
    if akcja == "zwiedzaj":
        if randint(0, 1) == 0:
            print(f"{Gracz.nazwa} znajduje jaskinie...")
        else:
            Przeciwnik = Przeciwnik(gracz)
            print(f"{gracz.nazwa} natrafia na {Przeciwnik.nazwa}")
            gra = gracz.walka(Przeciwnik)
    elif akcja == "odpocznij":
        gracz.odpoczynek()
    else:
        print("Wpisz jeszcze raz!")