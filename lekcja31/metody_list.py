#.get()
#.values()
#.items()
#.keys()
#.setdefault()
#.pop()
#.popitem()
#.clear()

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[::2])

"""
Napisz program w którym stworzysz listę z 10 liczbami, a następnie wypiszesz co
drugą z nich
"""

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for x in lista[0:10:2]:
#     print(x)

# for i in range(0, 10, 2):
#     print(lista[i])

# for j in range(10):
#     if j % 2 != 1:
#         print(lista[j])s

########################################
przykladowaLista = [8, "kot", 3, 3.5, "Trener", True]
print(przykladowaLista)

### .append() - Dodaje element do listy na jej końcu 
przykladowaLista.append("Python")
print(przykladowaLista)

### .extend() - Poszerza listę o dowolny element, po którym można iterować (lista, krotka, słownik, zbioru)
malaLista = [1, 2, 3]
przykladowaLista.extend(malaLista)
print(przykladowaLista)
### .insert() - Dodaje element do listy po wskazany indeks
nowyElement = 100
przykladowaLista.insert(1, nowyElement)
print(przykladowaLista)

### .pop() - Usuwa element spod wskazanego indeksu
przykladowaLista.pop() # bez żadnego argumentu usunie ostatni element
przykladowaLista.pop(0) # tutaj usuwa pod wskzazanym indeksem
print(przykladowaLista)

### .remove() - Usuwa dany element z listy przekazany wprost (Usuwa pierwszy napotkany element o podanej wartości)
przykladowaLista.remove("Trener")
print(przykladowaLista)

### .index()

### .count()
innaPrzykladowaLista = [1, 2, 3, 3, 1, 2, 4, 5, 6, 1, 3, 4, 6]

print("Trójek w liście jest:", innaPrzykladowaLista.count(3))
print("Czwórek w liście jest:", innaPrzykladowaLista.count(4))
print("Ósemek w liście jest:", innaPrzykladowaLista.count(8))

### .sort()
innaPrzykladowaLista.sort()
print("Posortowana lista:", innaPrzykladowaLista)

### .reverse()

innaPrzykladowaLista.sort(reverse=True)
print("Posortowana lista malejąco:", innaPrzykladowaLista)

