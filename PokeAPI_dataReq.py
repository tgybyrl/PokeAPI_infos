import requests
#from bs4 import BeautifulSoup

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data['name'],
            "height": pokemon_data['height'],
            "weight": pokemon_data['weight'],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]]
        }
        return pokemon_info
    else:
        return None

pokemon_name = input("Choose your pokemon: ")
pokemon_info = get_pokemon_info(pokemon_name)

#print(pokemon_info)

def result_stats():
    if pokemon_info:
        print(f"Name: {pokemon_info['name']}")
        print(f"Height: {pokemon_info['weight']}")
        print(f"Height: {pokemon_info['height']}")
        print(f"Abilities: {', '.join(pokemon_info["abilities"])}")
        print(f"Types: {', '.join(pokemon_info["types"])}")
    else:
        print("Pokemon not found!")

result_stats()