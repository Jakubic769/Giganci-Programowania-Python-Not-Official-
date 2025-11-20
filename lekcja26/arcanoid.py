import pygame

from platforma import Platforma
from kulka import Kulka
from klocek import Klocek

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
zycia = 3
poziom = 1

#poziomy gry
poziom1 = [
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
poziom2 = [
    [0, 0, 1, 2, 3, 3, 2, 1, 0, 0],
    [0, 1, 1, 1, 2, 2, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 0, 0, 2, 0, 2, 0]
]
poziom3 = [
    [2, 3, 2, 2, 2, 2, 2, 2, 3, 2],
    [2, 1, 3, 1, 1, 1, 1, 3, 1, 2],
    [2, 3, 1, 3, 1, 1, 3, 1, 3, 2],
    [3, 2, 2, 2, 3, 3, 2, 2, 2, 3],
    [0, 0, 2, 2, 3, 3, 2, 2, 0, 0],
    [0, 0, 2, 0, 3, 3, 0, 2, 0, 0],
    [0, 0, 3, 0, 3, 3, 0, 3, 0, 0]
]


def dodaj_klocki():
    wczytany_poziom = None
    if poziom == 1:
        wczytany_poziom = poziom1
    elif poziom == 2:
        wczytany_poziom = poziom2
    elif poziom == 3:
        wczytany_poziom = poziom3
    
    for i in range(10):
        for j in range(7):
            if wczytany_poziom[j][i] != 0:
                klocek = Klocek(32+i*96, 32+j*48, wczytany_poziom[j][i])
                klocki.add(klocek)


pygame.init()
pygame.font.init()

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
czcionka = pygame.font.SysFont("Comic Sans MS", 24)

obraz_tla = pygame.image.load("lekcja26/images/background.png")
platforma = Platforma()
kulka = Kulka()
klocki = pygame.sprite.Group()
dodaj_klocki()

gra_trwa = True
while gra_trwa:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_trwa = False
        elif zdarzenie.type == pygame.QUIT:
            gra_trwa = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        platforma.ruszaj_platforma(-1)
    if keys[pygame.K_d]:
        platforma.ruszaj_platforma(1)
        
    if len(klocki.sprites()) == 0:
        poziom += 1
        if poziom >= 3:
            break
        kulka.reset_pozycji()
        platforma.reset_pozycji()
        dodaj_klocki()
        
    kulka.aktualizuj(platforma, klocki)
    if kulka.przegrana:
        zycia -= 1
        if zycia <= 0:
            break
        kulka.reset_pozycji()
        platforma.reset_pozycji()
    
    platforma.aktualizuj()
    klocki.update()
            
    ekran.blit(obraz_tla, (0,0))
    for klocek in klocki:
        ekran.blit(klocek.obraz, klocek.rect)   
    ekran.blit(platforma.obraz, platforma.rect)
    ekran.blit(kulka.obraz, kulka.rect)
    
    tekst = czcionka.render(f"Życia: {zycia}", False, (255, 0, 255))
    ekran.blit(tekst, (16, 16))
    
    pygame.display.flip()
    zegar.tick(30)
    
pygame.quit()