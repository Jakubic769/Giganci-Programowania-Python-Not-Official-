translator = {
    "plus": '+',
    "dodać": '+',
    "odjąć": '-',
    "minus": '-',
    "podzielić": '/',
    "pomnożyć": '*',
    "zero": '0',
    "jeden": '1',
    "dwa": '2',
    "trzy": '3',
    "cztery": '4',
    "pięć": '5',
    "sześć": '6',
    "siedem": '7',
    "osiem": '8',
    "dziewięć": '9',
    "dziesięć": '10'
}

x = input("Podaj wyrażenie matematyczne (np. 'dwa plus dwa'): ").split()

# Pobranie i konwersja wartości na liczby całkowite
a = int(translator[x[0]])
op = translator[x[1]]
b = int(translator[x[2]])

# Obliczenie wyniku
if op == '+':
    wynik = a + b
elif op == '-':
    wynik = a - b
elif op == '*':
    wynik = a * b
elif op == '/':
    wynik = a / b
# Wyświetlenie wyniku
print(f"Wynik: {int(wynik)}")
