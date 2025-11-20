# napiszmy funkcję range:
 
# funkcja range przyjmuje 3 argumenty:
# 1. start (wymagany)
# 2. stop (wymagany)
# 3. wartość inkremementacji (opcjonalny, domyślnie 1, musi być dodatn)
 
# zwraca listę elementów w podanym zakresie
 
def my_range(start, stop, inkrementacja=1):
    lista_elementow = []
    element = start
    while element < stop:
        lista_elementow.append(element)
        element += inkrementacja
 
    return lista_elementow
 
zakres = my_range(1, 10, 1)
print(zakres)
 
# print(my_range(1, 10, 4) == list(range(1, 10, 4)))