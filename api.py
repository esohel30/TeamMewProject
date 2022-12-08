import requests
from random import Random

# For SuperHero api

superhero_key = ""
superherostarturl = "https://superheroapi.com/api/" + superhero_key + "/"

def generatecharacterquestion():
    idlist = range(1,732) #maybe modify this list later to remove certain characters from being chosen
    charid = Random.choice(idlist)
    req = requests.get(superherostarturl + charid)
    info = req.json()
    name = info['name']
    img = info['image']['url']

# For pokeapi

pokestarturl = "https://pokeapi.co/api/v2/pokemon/"

def generatepokemonquestion():
    pokeid = Random.nextint(1,906)
    req = requests.get(pokestarturl + pokeid)
    info = req.json()
    name = info['forms'][0]['name']
    img = info['sprites']['front_default']
    # check for how many types the pokemon has here and then add based on if it has 1 or 2 types
    poketype = []