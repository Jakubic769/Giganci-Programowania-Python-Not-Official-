# napiszmy funkcje, ktora przyjmuje 3 argumenty

#imie - str
#wzrost - float
#wiek - int

#celem tej funkcji jest wypisanie komunikatu "Jestem {imie, mam {wzrost}m, i mam {wiek} lat"

def min_i_max(a: int, b: int, c: int, d: int):
    return min(a, b, c, d), max(a, b, c, d)

liczba_min, liczba_max = min_i_max(1, 2, 3, 4)
print(liczba_min, liczba_max)
