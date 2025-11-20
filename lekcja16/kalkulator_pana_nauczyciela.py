# Inteligentny kalkulator:
# Chcemy, aby przyjmował on polecenia w formie:
# "pięć dodać szestaście",
# "cztery plus osiem" itd.

# Chcemy aby wynikiem działania programu było:

# "pięć dodać szestaście"
# 5 + 16 = 21

# Planowanie

# 1. Przyjęcie danych od użytkownika
# 2. Rozpoznanie danych - translacja słów na liczby
#    i operacji matematycznych na znaki:
#       - utworzenie słownika tłumaczącego słowo na liczbę/operację matematyczną
#       - wyodrębnienie poszczególnych słów z inputu użytkownika
#       - konstrukcja if/else aby wykonywać odpowiednie
#         działania na podstawie znalezionego znaku
# 3. Wyliczenie wyniku i wyprintowanie go.

# rozbudować nasz translator o pozostałe tłumaczenia (liczby od 1 do 10, =, -, /, *)
translator = {
    "plus": '+',
    "minus": '-',
    "podzielić": '/',
    "pomnożyć": '*',
    "zero": 0,
    "jeden": 1,
    "dwa": 2,
    "trzy": 3,
    "cztery": 4,
    "pięć": 5,
    "sześć": 6,
    "siedem": 7,
    "osiem": 8,
    "dziewięć": 9,
    "dziesięć": 10
}

# odczytać od użytkownika dane wejściowe
opis_dzialania = input("Co mam obliczyć?\t")

# zamienić dane od użytkownika ze str na listę str (.split(' '))
lista_slow = opis_dzialania.split(' ')

# dla każdego elementu z listy odnaleźć poprawne
# tłumaczenie słowa na wartość lub znak matematyczny
# for i in range(len(lista_slow)):
#    slowo = lista_slow[i]

tlumaczenie = []
for slowo in lista_slow:
    if slowo in translator.keys():  # jeśli słowo znajduje się wśród znanych tłumaczeń
        tlumaczenie.append(translator[slowo])
   
# w zależności od znaku operacji matematycznej znajdującej się w przetłumaczonej liście,
# bedziemy chcieli wykonać odpowiednie działanie

if '+' in tlumaczenie:
    tlumaczenie.remove('+')
    print(f"{tlumaczenie[0]} + {tlumaczenie[1]} = {tlumaczenie[0] + tlumaczenie[1]}")
elif '-' in tlumaczenie:
    tlumaczenie.remove('-')
    print(f"{tlumaczenie[0]} - {tlumaczenie[1]} = {tlumaczenie[0] - tlumaczenie[1]}")
elif '*' in tlumaczenie:
    tlumaczenie.remove('*')
    print(f"{tlumaczenie[0]} * {tlumaczenie[1]} = {tlumaczenie[0] * tlumaczenie[1]}")
elif '/' in tlumaczenie:
    tlumaczenie.remove('/')
    print(f"{tlumaczenie[0]} / {tlumaczenie[1]} = {tlumaczenie[0] / tlumaczenie[1]}")
else:
    print("Nie jesteśmy w stanie tego policzyć")