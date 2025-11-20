import re

def create_string(code):
    print("Zadanie 1:")
    letter = re.findall(r'\D+',code)
    numbers = re.findall(r'\d+',code)

    string = "".join([l*int(n) for l,n in zip(letter,numbers)])
    print(string)

create_string('e4lenjd55o6e')

def find_unique(string):
    unique_letter = [i for i in string if string.count(i) == 1]
    return(unique_letter[0])
#1
find_unique_letter = find_unique('ala ma kota, kota jest ali')
print(find_unique_letter)

#2
print(find_unique("ala ma kota, kota jest ali"))

def add(a,b):
    return a + b
print(add(1,2))

lambda_add = lambda x,y:x+y
print(lambda_add(1,2))

def sort_square(table):
    return sorted(table, key = lambda x: x*x)

print(sort_square([1, -2,0,4,-5]))

lista = [1, -2,0,4,-5]
print(sort_square(lista))

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 4))

def print_city_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_city_info(name="Warsaw", population=1790658, country="Poland", currency="PLN")

def rpg_postac(*imiona, **klasy):
    
    nazwa = " ".join(imiona)
    print(f"Postać: {nazwa}")
    
    
    print("Klasy i poziomy:")
    for klasa, poziom in klasy.items():
        print(f" - {klasa}: {poziom}")


rpg_postac("Arthas", "Bane", "of", "Light",
           Wojownik=10, Mag=5, Paladyn=7)


def gen(limit):
    counter = 0
    while counter < limit:
        yield counter
        counter += 1


# użycie
for x in gen(5):
    print(x)

