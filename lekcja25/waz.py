import pygame
import copy
from kierunek import Kierunek
from segment import Segment


class Waz(pygame.sprite.Sprite):
    def __init__(self):
        self.oryginalny_obraz = pygame.image.load("lekcja25/images/head.png")
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, 0)
        self.rect = self.obraz.get_rect(center=(12*32+16, 9*32+16))
        self.kierunek = Kierunek.GORA
        self.nowy_kierunek = Kierunek.GORA
        self.ostatnia_pozycja = self.rect
        self.dodaj_segment = False
        self.segmenty = []

    def zmien_kierunek(self, kierunek):
            zmiana_mozliwa = True
            if self.kierunek == Kierunek.GORA and kierunek == Kierunek.DOL:
                zmiana_mozliwa = False
            elif self.kierunek == Kierunek.DOL and kierunek == Kierunek.GORA:
                zmiana_mozliwa = False
            elif self.kierunek == Kierunek.PRAWO and kierunek == Kierunek.LEWO:
                zmiana_mozliwa = False
            elif self.kierunek == Kierunek.LEWO and kierunek == Kierunek.PRAWO:
                zmiana_mozliwa = False 
            if zmiana_mozliwa == True:
                self.nowy_kierunek = kierunek
            
    def aktualizuj(self):
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, (self.kierunek.value*-90))
        
        self.ostatnia_pozycja = copy.deepcopy(self.rect)
        if self.kierunek == Kierunek.GORA:
            self.rect.move_ip(0, -32)
        elif self.kierunek == Kierunek.DOL:
            self.rect.move_ip(0, 32)
        elif self.kierunek == Kierunek.LEWO:
            self.rect.move_ip(-32, 0)
        elif self.kierunek == Kierunek.PRAWO:
            self.rect.move_ip(32, 0)
            
        for i in range(len(self.segmenty)):
            if i == 0:
                self.segmenty[i].przesun(self.ostatnia_pozycja)
            else:
                self.segmenty[i].przesun(self.segmenty[i-1].ostatnia_pozycja)
                
        if self.dodaj_segment:
            nowy_segment = Segment()
            nowa_pozycja = None
            if len(self.segmenty) > 0:
                nowa_pozycja = copy.deepcopy(self.segmenty[-1].ostatnia_pozycja)
            else:
                nowa_pozycja = copy.deepcopy(self.ostatnia_pozycja)
            nowy_segment.pozycja = nowa_pozycja
            self.segmenty.append(nowy_segment)
            self.dodaj_segment = False
            
    def rysuj_segmenty(self, ekran):
        for segment in self.segmenty:
            ekran.blit(segment.obraz, segment.pozycja)
            
    def jedz_jablko(self):
        self.dodaj_segment = True
    
    def sprawdz_kolizje(self):
        for segment in self.segmenty:
            if self.rect.topleft == segment.pozycja.topleft:
                return True
            
        if self.rect.top < 0 or self.rect.top >= 608:
            return True
        if self.rect.left < 0 or self.rect.left >= 800:
            return True