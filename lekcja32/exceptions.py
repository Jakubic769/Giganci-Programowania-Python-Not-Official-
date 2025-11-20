#import openai
#import time

#krotka = (1, 2, 3)

#krotka.pop(1)

#print(cos)

#for _ in range(100):
#    time.sleep(10)

def dzielenie(a: float, b: float) -> float:
    try:
        return a/b
    except ZeroDivisionError:
        return "Dzielisz przez 0"
    except TypeError:
        return "Sprawdź typy tych liczb!"


print(dzielenie(2.2, "1"))

import random

wybor = ["Hiszpania", "Portugalia", "Włochy", "Francja", "Chiny", "Szwecja"]

for i  in range(6):
    cel = random.choice(wybor)
    wybor.remove(cel)
    if cel != "Francja":
        print(f"Ja lecę do {cel}")
    else:
        raise Exception("Ale ja nie chce do Francji *-*")
