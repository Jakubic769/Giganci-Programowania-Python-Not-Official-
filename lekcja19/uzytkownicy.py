class Uzytkownik:
    
    def __init__(self, imie: str, nick: str, wiek: int):
        self.imie = imie
        self.nick = nick
        self.wiek = wiek


    def przywitanie_z_user(self):
        print(f"Witaj! {self.imie}, twój nick to {self.nick} i w tej chwili masz {self.wiek} lat")