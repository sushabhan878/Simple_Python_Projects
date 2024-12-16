# Creating a simple pokemon detail finder using POKEAPI. 
# Website link:  https://pokeapi.co/?ref=public-apis


import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Data Retrieved !   ")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to Retrieved Data ! {response.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)
print(pokemon_info)