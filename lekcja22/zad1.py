class Zwierze:
    
    def __init__(self, wiek: int, imie: str, waga: float):
        self.wiek = wiek
        self.imie = imie
        self.waga = waga
        
    def wypisz_imie(self):
        print(f"Mam na imię {self.imie}.")
        
    def wypisz_wiek(self):
        print(f"Mam obecnie {self.wiek} lat.")
        
    def wypisz_wage(self):
        print(f"Moja waga to {self.waga} kg.")
        
        
class Pies(Zwierze):
    def __init__(self, wiek: int, imie: str, waga: float, zarcie: str):
        super().__init__(wiek, imie, waga)
        self.zarcie = zarcie

    def co_pies_je(self):
        print(f"Psy jędzą {self.zarcie}")
    
zwierzak = Zwierze(8, "Białas", 15)
zwierzak.wypisz_imie()
zwierzak.wypisz_wiek()
zwierzak.wypisz_wage()

Pies = Pies(8, "clank", 9.7, "karme dla psów") #nie znam się na psach
Pies.wypisz_imie()
Pies.wypisz_wiek()
Pies.wypisz_wage()
Pies.co_pies_je()