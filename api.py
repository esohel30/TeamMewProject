import requests
from random import Random

# For SuperHero api

superhero_key = ""
superherostarturl = "https://superheroapi.com/api/" + superhero_key

def chooserandcharacter():
    

# For pokeapi

pokestarturl = "https://pokeapi.co/api/v2/pokemon/"

def chooserandpokemon():
    pokeid = Random.nextint(1,906)
    req = requests.get(pokestarturl + pokeid)
    info = req.json()
    name = info['forms'][0]['name']
    img = info['sprites']['front_default']
    # check for how many types the pokemon has here and then add based on if it has 1 or 2 types
    poketype = []