import pygame
from Element import *


SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

obraz_tlo = pygame.image.load("images/obraz.png")
obraz_baza_postaci = pygame.image.load("images/base.png")

pygame.font.init()
moja_czcionka = pygame.font.SysFont("Comic Sans MS", 30)

pygame.init()

def wypisz_tekst(ekran, tekst, pozycja):
    napis = moja_czcionka.render(tekst, False, (255, 255, 255))
    ekran.blit(napis, pozycja)

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

gra_trwa = True
zapisywanie = False

ubrania = UbraniaElement()
oczy = OczyElement()
bronie = BronElement()
glowa = NakrycieGlowy()


while gra_trwa:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_trwa = False
            if zdarzenie.key == pygame.K_q:
                glowa.wybierzNastepny()
            if zdarzenie.key == pygame.K_w:
                oczy.wybierzNastepny()
            if zdarzenie.key == pygame.K_e:
                ubrania.wybierzNastepny()
            if zdarzenie.key == pygame.K_r:
                bronie.wybierzNastepny()
            if zdarzenie.key == pygame.K_s:
                zapisywanie = True
        if zdarzenie.type == pygame.QUIT:
            gra_trwa = False
            
    ekran.blit(obraz_tlo, (0, 0))
    ekran.blit(obraz_baza_postaci, (270, 130))
    
    ekran.blit(ubrania.wybranyObraz(), (270, 130))
    ekran.blit(oczy.wybranyObraz(), (270, 130))
    ekran.blit(bronie.wybranyObraz(), (270, 130))
    ekran.blit(glowa.wybranyObraz(), (270, 130))
    
    if zapisywanie:
        pygame.image.save(ekran, 'postac.png')
        zapisywanie = False
    
    wypisz_tekst(ekran, f'[Q] Glowa: {glowa.wybrany}', (100, 100))
    wypisz_tekst(ekran, f'[W] Oczy: {oczy.wybrany}', (100, 140))
    wypisz_tekst(ekran, f'[E] Stroj: {ubrania.wybrany}', (100, 180))
    wypisz_tekst(ekran, f'[R] Bron: {bronie.wybrany}', (100, 220))
    wypisz_tekst(ekran, f'[S] Zapisz', (100, 260))

    pygame.display.flip()
    zegar.tick(30)

pygame.quit()