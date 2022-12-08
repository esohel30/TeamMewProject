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

def generatepokemonquestion(): #Some pokemon names will have a "-" in the name, we should let the user get the question correct even if they don't include the "-" or anything past it.
    pokeid = randint(1,906)
    pokeurl = startpokeurl + (str)(pokeid)
    req = requests.get(pokeurl)
    info = req.json()
    name = info['forms'][0]['name']
    img = info['sprites']['front_default']
    # choose what type of question to generate
    qtype = randint(0,1)
    if qtype == 0: #What is this pokemon's type(s)?
        answer = []
        # check for how many types the pokemon has here and then add based on if it has 1 or 2 types
        if len(info['types']) == 2:
            answer += [info['types'][0]['type']['name'], info['types'][1]['type']['name']]
        else:
            answer += [info['types'][0]['type']['name']]
        question = "What is this pokemon's type(s)"
    if qtype == 1:
        question = "What is the name of this pokemon?"
        answer = name
    packagedinfo = [name, img, qtype, question, answer]
    print(packagedinfo)
    
generatepokemonquestion()