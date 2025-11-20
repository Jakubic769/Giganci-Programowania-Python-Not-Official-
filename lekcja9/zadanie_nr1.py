oceny = []
 
while True:
    komunikat = input("Podaj ocenę. Aby zakończyć wpisz 'q'")
 
    if komunikat == "q":
        break
    ocena_czastkowa = int(komunikat)
 
    oceny.append(ocena_czastkowa)
 
suma_ocen = sum(oceny)
ilosc_ocen = len(oceny)
srednia = suma_ocen/ilosc_ocen
print(srednia)

