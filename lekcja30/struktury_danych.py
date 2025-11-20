# krotki

krotka = (1, 2, 3, 4, 5, 6, 7, 8, 9)
krotka_jednoelementowa = (1, )
print(type(krotka_jednoelementowa))
print(krotka_jednoelementowa)

print(krotka[:5])

print(krotka.count(1))

print(krotka[4], krotka.index(6))

zbior = {1, 2, 3, 4, 5, 6, 6, 6, 6}
print(zbior)

zbior.add(10)
print(zbior)

zbior.remove(1)
print(zbior)
zbior.discard(9)
print(zbior)
zbior.discard(2)
print(zbior)

zbior.clear()
print(zbior)

zbior1 = {1, 4, 2, 6, 7, 3, 4}
zbior2 = {2, 1, 6, 5, 3, 4, 2}

print(zbior1.difference_update(zbior2))
print(zbior2.difference_update(zbior1))

print(zbior1)
print(zbior2)

krotka = (1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1)
zbior = {1, 2, 3, 4, 5, 6, 8, 9}
lista = [1, 3, 2, 5, 6, 3, 2, 2, 1]

print(list(zbior))
print(list(krotka))

print(set(krotka))
print(set(lista))

print(tuple(krotka))
print(tuple(lista))

for i in range(len(zbior)):
    pass

for i in zbior:
    pass