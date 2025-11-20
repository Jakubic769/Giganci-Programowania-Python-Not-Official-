import pygame
import random

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800

vec = pygame.math.Vector2


class Kulka(pygame.sprite.Sprite):
    def __init__(self):
        super(Kulka, self).__init__()
        self.obraz = pygame.image.load("lekcja26/images/ball.png")
        self.r = 16
        self.reset_pozycji()

    def reset_pozycji(self):
        self.wspolrzedne = vec(SZEROKOSC_EKRANU/2, WYSOKOSC_EKRANU - 140)
        self.rect = self.obraz.get_rect(center=self.wspolrzedne)
        self.wektor = vec(0, -10)
        self.kat_nachylenia = random.randrange(-30, 30)
        self.wektor.rotate_ip(self.kat_nachylenia)
        self.przegrana = False

    def aktualizuj(self, platforma, klocki):
        self.wspolrzedne += self.wektor
        self.rect.center = self.wspolrzedne
        self.sprawdz_kolizje(platforma, klocki)

    def sprawdz_kolizje(self, platforma, klocki):
        if self.rect.x <= 0:
            self.wektor.x *= -1
        if self.rect.right >= SZEROKOSC_EKRANU:
            self.wektor.x *= -1
        if self.rect.y <= 0:
            self.wektor.y *= -1
        if self.rect.bottom >= SZEROKOSC_EKRANU:
            self.przegrana = True

        if self.rect.colliderect(platforma.rect):
            self.wektor.y *= -1
            self.wektor.x += platforma.porusza_sie*5
            if self.wektor.x < -10:
                self.wektor.x = -10
            if self.wektor.x >10:
                self.wektor.x = 10

        for klocek in klocki:
            if self.kolizja_z_klockiem(self, klocek):
                klocek.uderzenie()
                break

    def kolizja_z_klockiem(self, kulka, klocek):
        dystant_x = abs(kulka.rect.centerx - klocek.rect.centerx) - klocek.rect.w / 2
        dystant_y = abs(kulka.rect.centery - klocek.rect.centery) - klocek.rect.h / 2

        if dystant_x < kulka.r and dystant_y < kulka.r:
            if dystant_x < dystant_y:
                self.wektor.y *= -1
            else:
                self.wektor.x *= -1
            return True
        return False
    #dziękuje :)