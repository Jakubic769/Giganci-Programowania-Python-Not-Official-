import pygame

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800

class Platforma(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obraz = pygame.image.load("lekcja26\images\pad.png")
        self.reset_pozycji()
        self.porusza_sie = 0

    def reset_pozycji(self) -> pygame.Rect:
        self.rect = pygame.Rect(SZEROKOSC_EKRANU/2 - 140/2, WYSOKOSC_EKRANU - 70, 140, 30)
        
    def ruszaj_platforma(self, wartosc):
        predkosc = 10
        self.rect.move_ip(wartosc*predkosc, 0)
        self.porusza_sie = wartosc
        if self.rect.left <= 0:
            self.rect.x = 0
        if self.rect.right >= SZEROKOSC_EKRANU:
            self.rect.x = SZEROKOSC_EKRANU - 140
    
    def aktualizuj(self):
        self.porusza_sie = 0
