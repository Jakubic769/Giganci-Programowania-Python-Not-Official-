#6. Dodaj do listy elementy z krotki, zbioru i wartości słownika.

lista = [1, 2]
krotka = (3, 4)
zbior = {5, 6}
slownik = {'a': 7, 'b': 8}

lista.extend(krotka)
lista.extend(zbior)
lista.extend(slownik.values())


print("Lista po dodaniu elementów:")
print(lista)
