# Connect to an API using python 

import requests

base_url = "https://pokeapi.co/api/v2/"

def pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    # return response

    if response.status_code == 200:
        pokemon = response.json()
        return pokemon
    else:
        print(f"Failed to retrieve data {response.status_code}")


get_pokemon = pokemon_info("pikachu")

if  get_pokemon:
    print(f"    Name           = {get_pokemon["name"]}")
    print(f"    Height         = {get_pokemon["height"]}")
    print(f"    Weight         = {get_pokemon["weight"]}")

    for a in get_pokemon["abilities"]:
        if a["is_hidden"]:
            print(f" Special Ability   = {a['ability']['name']}")