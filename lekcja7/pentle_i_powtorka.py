import time
#liczba = int(input("Wpisz liczbę całkowitą np. 67\n"))
#print("Myślenie komputera")
#time.sleep(1)
#print("...")
#time.sleep(1)
#print("Gotowe!")
#time.sleep(1)
#
#if liczba % 3 == 0:
#    print("twoja liczba jest podzielna przez 3")
#else:
#    print("twoja liczba nie jest podzielna przez 3")
#
#time.sleep(1)
#
#if liczba % 7 == 0:
#    print("twoja liczba jest podzielna przez 7")
#else:
#    print("twoja liczba nie jest podzielna przez 7")
#
#time.sleep(1)
#
#if liczba % 31 == 0:
#    print("twoja liczba jest podzielna przez 31")
#else:
#    print("twoja liczba nie jest podzielna przez 31")
#
#time.sleep(1)
#
#if liczba % 3 == 0 and liczba % 7 == 0 and liczba % 31 == 0:
#    print("twoja liczba jest podzielna przez wszystkie liczby!!!")
#else:
#    print("twoja liczba nie jest podzielna przez wszystkie liczby!!!")

liczba =  int(input("\rPodaj ile czasu zostało do detonacji bomby!\n"))
liczba -= 1
while liczba >= 0:
    time.sleep(1)
    print("\r" + str(liczba), end= '')
    liczba -= 1

print("\rBOOM!!!")



