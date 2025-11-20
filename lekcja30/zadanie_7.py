#7. Dodaj do listy 2 liczby - wartość maksymalna i minimalna listy.

lista = [1, 2, 3, 4, 5, 6, 7, 8]

maks = max(lista)
minim = min(lista)

lista.append(maks)
lista.append(minim)

print("Lista po dodaniu wartości maksymalnej i minimalnej:")
print(lista)
