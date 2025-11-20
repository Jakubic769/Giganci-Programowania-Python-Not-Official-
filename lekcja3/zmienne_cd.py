bitwa_pod_grunwaldem = 1410
chrzest_polski = 966
powstanie_warszawskie = 1944

# ==
# >
# <
# >=
# <=

###print(bitwa_pod_grunwaldem == chrzest_polski)
###print(chrzest_polski <= powstanie_warszawskie)
###print(powstanie_warszawskie >= bitwa_pod_grunwaldem )

zmienna_a = 13
zmienna_b = 19

# + plus
# - minus
# * mnozyc
# / dzielic

# przyklad dzielenia
###wynik_dzielenia = zmienna_a / zmienna_b
###print(wynik_dzielenia)

# troszkę ciekawsze operatory

# % - modulo

###wynik_modulo = zmienna_b % 2
###print(wynik_modulo)

# // -

wynik_dzielenia_staloprzeciwnkowego = zmienna_b // zmienna_a
###print(type(wynik_dzielenia_staloprzeciwnkowego))

numer_pesel = 11948564712
numer_pesel_bez_ostatniej_cyfry = numer_pesel // 10
###print("numer_pesel_bez_ostatniej_cyfry: ", numer_pesel_bez_ostatniej_cyfry)

plec = numer_pesel_bez_ostatniej_cyfry % 2
###print(plec)

# ** - potegowanie
###print(3**3)

# inkrementacja - zwiekszanie wartosci
# dekrementacja - zmniejszanie wartosci

# inkrementacja przyklad
liczpa_wpisow = 1
liczpa_wpisow += 4

###print(liczpa_wpisow)

# dekrementacja przyklad

###minuty_do_konca_meczu = 90
###minuty_do_konca_meczu -= 1

###print(minuty_do_konca_meczu)

###print(zmienna_a+zmienna_b)
###print(zmienna_b-zmienna_a)
###print(zmienna_a**zmienna_b)


###print(True+True) # <- to widzimy i wynikiem jest 2
###print(int(True+int(True)))
###print(False+False)

warunek1 = False
warunek2 = False
warunek3 = True

###print(bool(warunek1*warunek2*warunek3))

###print(bool(warunek1+warunek2+warunek3))


# zadanie 1
###print("Witaj, jestem python!\nJak ty masz na imię!")
###imie = input()
###print("A na nazwisko??")
###nazwisko = input()
###urodziny = int(input("Kiedy się urodziłeś?\n"))
###wiek = 2024 - urodziny

###print(f"Cześć {imie} {nazwisko} Miło cię poznac masz {wiek} lat!")

# zadanie 2

# 1 sposob
##def sum(a, b):
##    return (a + b)

##a = int(input('wpisz 1 liczbe: '))
##b = int(input('wpisz 1 liczbe: '))

##print(f'suma z {a} i {b} to {sum(a, b)}')

# 2 sposob

c = int(input('wpisz 1 liczbe: '))
d = int(input('wpisz 2 liczbe: '))

wynik = c + d

print(f'suma z {c} i {d} to {wynik}')

##print(12==15)
##print(5<15000)
##print(120<120)
##print(60<15)
##print(25.3421<=25.3421)
