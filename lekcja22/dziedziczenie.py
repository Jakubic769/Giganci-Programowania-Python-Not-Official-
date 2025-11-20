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
        
        
class Kot(Zwierze):
    
    """
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
    """
    
    def __init__(self, wiek: int, imie: str, waga: float, dzwiek: str):
        super().__init__(wiek, imie, waga)
        self.dzwiek = dzwiek

    def wydawany_dzwiek(self):
        print(f"Koty wydają taki dźwięk jak {self.dzwiek}")
    
        
zwierzak = Zwierze(3, "Aro", 2)
zwierzak.wypisz_imie()
zwierzak.wypisz_wiek()
zwierzak.wypisz_wage()

kot = Kot(5, "Balbina", 4.5, "miauczenie")
kot.wypisz_imie()
kot.wypisz_wiek()
kot.wypisz_wage()
kot.wydawany_dzwiek()
