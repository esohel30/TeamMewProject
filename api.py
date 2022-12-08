import requests
from random import randint, choice
# For SuperHero api
superhero_key = ""
startsuperherourl = "https://superheroapi.com/api/" + superhero_key + "/"

'''
def generatecharacterquestion():
    idlist = range(1,732) #maybe modify this list later to remove certain characters from being chosen
    charid = choice(idlist)
    superherourl = startsuperherourl + (str)(charid)
    req = requests.get(superherourl)
    info = req.json()
    name = info['name']
    img = info['image']['url']
'''
# For pokeapi

startpokeurl = "https://pokeapi.co/api/v2/pokemon/"

def generatepokemonquestion():
    pokeid = randint(1,906)
    pokeurl = startpokeurl + (str)(pokeid)
    req = requests.get(pokeurl)
    info = req.json()
    name = info['forms'][0]['name']
    img = info['sprites']['front_default']
    # check for how many types the pokemon has here and then add based on if it has 1 or 2 types
    poketype = []
    if len(info['types']) == 2:
        poketype += [info['types'][0]['type']['name'], info['types'][1]['type']['name']]
    else:
        poketype += [info['types'][0]['type']['name']]
    # choose what type of question to generate
    
    print(poketype)
    print(name)
    
generatepokemonquestion()



''' 
# Set the base URL for the PokeAPI
base_url = "https://pokeapi.co/api/v2/pokemon/"

# Ask the user for the name of the Pokemon they want to get stats for
pokemon_name = input("Enter the name of the Pokemon you want to get stats for: ")

# Send a GET request to the PokeAPI to get the Pokemon's data
response = requests.get(base_url + pokemon_name.lower())

# Get the Pokemon's stats from the response
stats = response.json()["stats"]

# Print the Pokemon's stats
print(f"{pokemon_name}'s stats:")
for stat in stats:
    print(f"{stat['stat']['name']}: {stat['base_stat']}")


'''