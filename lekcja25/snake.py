import pygame
import random
import time
from jablko import Jablko
from waz import Waz
from kierunek import Kierunek

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608

pygame.init()

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

waz = Waz()

PORUSZ_WEZEM = pygame.USEREVENT + 1
pygame.time.set_timer(PORUSZ_WEZEM, 200)

tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))

jablka = pygame.sprite.Group()

for _ in range(5):
    jablko = Jablko()
    jablka.add(jablko)


for x in range(25):
    for y in range(19):
        obraz = pygame.image.load("lekcja25/images/background.png")
        maska = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))

        obraz.fill(maska, special_flags=pygame.BLEND_RGB_ADD)
        tlo.blit(obraz, (x*32, y*32))


gra_trwa = True
while gra_trwa:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_trwa = False
            if zdarzenie.key == pygame.K_w:
                waz.zmien_kierunek(Kierunek.GORA)
            if zdarzenie.key == pygame.K_s:
                waz.zmien_kierunek(Kierunek.DOL)
            if zdarzenie.key == pygame.K_a:
                waz.zmien_kierunek(Kierunek.LEWO)
            if zdarzenie.key == pygame.K_d:
                waz.zmien_kierunek(Kierunek.PRAWO)
    
        elif zdarzenie.type == PORUSZ_WEZEM:
            waz.aktualizuj()

        elif zdarzenie.type == pygame.QUIT:
            gra_trwa = False
    
    kolizja_z_jablkiem = pygame.sprite.spritecollideany(waz, jablka)
    if kolizja_z_jablkiem != None:
        kolizja_z_jablkiem.kill()
        waz.jedz_jablko()
        jablko = Jablko()
        jablka.add(jablko)

    ekran.blit(tlo, (0, 0))
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)
    ekran.blit(waz.obraz, waz.rect)
    waz.rysuj_segmenty(ekran)

    if waz.sprawdz_kolizje():
        gra_trwa = False

    pygame.display.flip()
    zegar.tick(30)

pygame.quit()