#3. Za pomocą pętli for wypisz wszystkie elementy każdego z obiektów

tekst = "Python"
print("Elementy tekstu:")
for znak in tekst:
    print(znak)

lista = [1, 2, 3, 4]
print("\nElementy listy:")
for element in lista:
    print(element)

krotka = (10, 20, 30)
print("\nElementy krotki:")
for element in krotka:
    print(element)

slownik = {'a': 1, 'b': 2}
print("\nElementy słownika (klucz: wartość):")
for klucz in slownik:
    print(f"{klucz}: {slownik[klucz]}")

zbior = {1, 2, 3}
print("\nElementy zbioru:")
for element in zbior:
    print(element)
