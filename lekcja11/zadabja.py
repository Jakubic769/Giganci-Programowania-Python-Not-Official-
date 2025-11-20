# zad1
# Napisz funkcję, która jako argument otrzymuje listę elementów, w której mogą
# występować powtórzenia, a zwraca listę unikalnych elementów.
# Dla [1,2,3,3,3,3,4,5] oczekujemy [1, 2, 3, 4, 5]
# lista_liczb = [1, 2, 3]
# print(4 in lista_liczb)

def unikalne_elementy(lista_liczba: list) -> list:
    lista_unikalnych_elementow = []
    for liczba in lista_liczba:
        if not liczba in lista_unikalnych_elementow:
            lista_unikalnych_elementow.append(liczba)
        
    return lista_unikalnych_elementow

# print(unikalne_elementy([1,2,3,3,3,3,4,5]))

# zad2
# Napisz funkcję, która otrzymuje liczbę całkowitą a zwraca sumę jej cyfr.
# Dla liczby 249 otrzymujemy 2+4+9 czyli 15

def suma_cyfr(liczba: int) -> int:
    suma = 0
    while liczba != 0:
        suma += liczba % 10
        liczba = liczba // 10
    return suma
        
# alternatywne podejście

def suma_cyfr1(liczba):
    # 249
    suma = 0
    for cyfra in str(liczba):   # "249"
        suma += int(cyfra)  # po kolei "2", "4", "9"
    return suma
        
    # return sum(int(cyfra) for cyfra in str(liczba))


wynik = suma_cyfr(249)
print(wynik)
wynik2 = suma_cyfr1(249)
print(wynik2)

# zad3
# Napisz funkcję, która zwraca listę losowych liczb. Rozmiar listy zależy od argumentu.
# Dodatkowo: Funkcja powinna otrzymać dwa dodatkowe argumenty: minimalna i
# maksymalna wartość, która może zostać wylosowana.

# podpowiedz - aby wylosować liczby losowe

# import random
# print(random.randint(1, 10)) # funkcja losująca losową liczbę w zakresie od 1 do 10 (bez dziesiątki)