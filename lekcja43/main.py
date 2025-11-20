import requests
from pprint import pprint

# Asystent podróży
# Api pogodowe - https://openweathermap.org/api
# Api z informacjami o krajach - https://restcountries.com/
# Api z informacjami o kursach walut - https://api.nbp.pl/#info


API_KEY = "2e22e77075449c748ee4ae327ae6d1c4"

def check_coordinates(city, API_KEY):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}')
    #print(response.status_code)
    #pprint(response.json())
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    #city = response.json()[0]['name']
    country = response.json()[0]['country']
    return lat, lon, country

def get_weather_info(lat,lon):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&limit=1&appid={API_KEY}&lang=PL&units=metric')
    #print(response.status_code)
    #pprint(response.json())
    response_json = response.json()
    weather = response_json['weather'][0]['description']
    temperature = response_json['main']['temp']
    pressure = response_json['main']['pressure']
    humidity = response_json['main']['humidity']
    return weather, temperature, pressure, humidity

def get_currency_code(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    response = requests.get(url)
    currency_code = list(response.json()[0]['currencies'].keys())[0]
    return currency_code

def get_country_full_name(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    response = requests.get(url)
    country_name = response.json()[0]['name']['common']
    return country_name

def get_currency_ratio(ori_curr, dest_curr):
    if ori_curr != "PLN":
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{ori_curr.lower()}/" 
        response = requests.get(url)    
        ori_ratio = response.json()['rates'][0]['mid']
    else:
        ori_ratio = 1

    if dest_curr != "PLN":
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{dest_curr.lower()}/" 
        response = requests.get(url)    
        dest_ratio = response.json()['rates'][0]['mid']
    else:
        dest_ratio = 1

    ratio = float(ori_ratio)/float(dest_ratio)
    return ratio

def print_weather_info(place):
    lat, lon, _ = check_coordinates(place, API_KEY)
    weather, temperature, pressure, humidity = get_weather_info(lat, lon)
    print(f"pogoda dla miasta {place}: {weather}")
    print(f"temperatura: {temperature}℃")
    print(f"Wilgotność: {humidity}%")
    print(f"Ciśnienie {pressure} hPa")

origin_place = None
destination_place = None

while True:
    print('''Jaką akcję chcesz wykonać?
                1.Podaj/zmień miejsce startowe
                2.Podaj/zmień miejsce docelowe
                3.Sprawdź lokalizację miejsca startowego
                4.Sprawdź lokalizację miejsca docelowego
                5.Sprawdź pogodę miejsca startowego
                6.Sprawdź pogodę miejsca docelowego
                7.Dowiedz się więcej o walucie
                8.Koniec''')
    choosen_option = int(input())
    
    if choosen_option == 1:
        origin_place = input("Podaj miasto startowe.\n")

    elif choosen_option == 2:
        destination_place = input("Podaj miasto docelowe.\n")

    elif choosen_option == 3:
        if origin_place is not None:
            lat, lon, country = check_coordinates(origin_place, API_KEY)
            country_name = get_country_full_name
            print(f"Miasto {origin_place} leży w kraju {country_name}")
            print(f"Długości geograficznej: {lon}, szerokość geograficzna: {lat}")
        else:
            print("Najpierw musisz podać miejsce startowe")

    elif choosen_option == 4:
        if destination_place is not None:
            lat, lon, country = check_coordinates(destination_place, API_KEY)
            country_name = get_country_full_name
            print(f"Miasto {destination_place} leży w kraju {country_name}")
            print(f"Długości geograficznej: {lon}, szerokość geograficzna: {lat}")
        else:
            print("Najpierw musisz podać miejsce docelowe")

    elif choosen_option == 5:
        if origin_place is not None:
            print_weather_info(origin_place)
        else:
            print("Najpierw musisz wpisać miasto startowe")

    elif choosen_option == 6:
        if destination_place is not None:
            print_weather_info(destination_place)
        else:
            print("Najpierw musisz wpisać miasto docelowe")

    elif choosen_option == 7:
        pass

    elif choosen_option == 8:
        quit()
    else:
        print("Error: Błędna opcja/opcja nie instnieje!")
    print("Naciśnij ENTER, aby kontynuować...")
    input()