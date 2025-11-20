# Kreator list


ile_elementow = int(input("Ile elementów chcesz mieć w liście? "))


lista = []


for i in range(ile_elementow):
    element = input(f"Podaj {i+1}. element: ")
    lista.append(element)  # Dodajemy element do listy


print("Oto Twoja lista:")
print(lista)
