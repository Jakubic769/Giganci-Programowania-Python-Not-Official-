suma = 0  

while True:
    wejscie = input("Podaj liczbę lub napisz 'koniec': ")
    if wejscie == "koniec" or "KONIEC" or "Koniec":
        break  
    
    suma += int(wejscie) 
print("Suma podanych liczb wynosi:", suma)

