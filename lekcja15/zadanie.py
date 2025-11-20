# Zadanie 1
# Napisz funkcję, która otrzyma jeden argument określający liczbę dziesiętną. Funkcja ma
# wyświetlić ile wynosi podana liczba w zapisie binarnym.

def binary(a):
    # Tworzymy pusty tekst, w którym będziemy przechowywać wynik w postaci binarnej
    wynik = ''
    
    # Powtarzamy dopóki liczba 'a' jest większa od 0
    while(a > 0):
        # Obliczamy resztę z dzielenia przez 2 (0 lub 1)
        m = a % 2
        
        # Dzielimy liczbę przez 2 i bierzemy tylko część całkowitą
        a = a // 2
        
        # Dodajemy resztę (jako tekst) na początek wyniku
        wynik = str(m) + wynik
    
    # Po zakończeniu pętli, wypisujemy liczbę w systemie binarnym
    print(wynik)

# Wywołanie funkcji z liczbą 41 jako argument
binary(41)