#5. Wypisz te same elementy w odwrotnej kolejności.

tekst = "Python"
print("Tekst w odwrotnej kolejności:")
for znak in reversed(tekst):
    print(znak)

lista = [1, 2, 3, 4]
print("\nLista w odwrotnej kolejności:")
for element in reversed(lista):
    print(element)

krotka = (10, 20, 30)
print("\nKrotka w odwrotnej kolejności:")
for element in reversed(krotka):
    print(element)

slownik = {'a': 1, 'b': 2, 'c': 3}
print("\nWartości słownika w odwrotnej kolejności:")
for wartosc in reversed(list(slownik.values())):
    print(wartosc)

zbior = {1, 2, 3}
print("\nZbiór w odwrotnej kolejności (po przekształceniu na listę):")
for element in reversed(list(zbior)):
    print(element)
