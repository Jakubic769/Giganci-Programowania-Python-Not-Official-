import requests
from bs4 import BeautifulSoup
from fpdf import FPDF


def scrap_pokemon_list():
    url='https://pokelife.pl/pokedex/index.php?title=Lista_Pokemon%C3%B3w_Kanto'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    pokemon_list = []
    
    table = soup.find('table', class_='Tabela1')
    rows = table.find_all('tr')
    rows = rows[1:]
    
    for row in rows:
        columns = row.find_all('td')
        pokemon = (columns[2].text[:-1], f"No.{columns[0].text[:-1]}")
        pokemon_list.append(pokemon)
        
    pokemon_list_without_mega = (pokemon for pokemon in pokemon_list if "Mega" not in pokemon[0] and "Gigantamax" not in pokemon[0])
    return pokemon_list_without_mega

def get_pokemon_info(pokemon_name):
    pokemon_name = pokemon_name.replace('\'','')
    pokemon_name = pokemon_name.replace('. ','-')
    pokemon_name = pokemon_name.replace('♀','-f')
    pokemon_name = pokemon_name.replace('♂','-m')
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)
    return response.json()

def get_pokemon_image(pokemon_info):
    link = pokemon_info['sprites']['front_default']
    return link

def get_pokemon_types(pokemon_info):
    types = []
    for item in pokemon_info['types']:
        type = item['type']['name']
        types.append(type)
    return types

pdf = FPDF()
pdf.add_font("DejaVu", "", "lekcja_44/dejavu-sans/DejaVuSans.ttf", uni=True)
    
pokemon_list = scrap_pokemon_list()
found_pokemon = []
for pokemon in pokemon_list:
    try:
        pokemon_info = get_pokemon_info(pokemon[0])
        image_url = get_pokemon_image(pokemon_info)
        img_data = requests.get(image_url).content
        pokemon_types = get_pokemon_types(pokemon_info)
        found_pokemon.append(pokemon)
    except:
        pass
    else:
        pdf.add_page(format = 'A5')
        pdf.set_font("DejaVu", size=16)
        pdf.text(x=5, y = 10, text=f"#{pokemon[1]} {pokemon[0]}")
        pdf.image(img_data, x=30, y=10, w=100, h = 100 )
        pdf.set_font("DejaVu", size=12)
        type_tekst = ''.join(str(type)+', ' for type in pokemon_types)
        pdf.text(x = 50, y = 120, text=f"Typ: {type_tekst[:-2]}")

pdf.output("pokedex.pdf")