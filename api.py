import requests
from random import randint, choice

# Returns a list that contains information to be put on the site in the following form:
# [statname, [char1name, char1imgurl, char1stat], [char2name, char2imgurl, char2stat]]
def generatecharacterquestion():
    statlist = ["intelligence", "strength", "speed", "durability", "power", "combat"]
    whatstat = randint(2,7)
    statname = statlist[(whatstat - 2)] # The stat that is being compared
    idlist = list(range(1,732)) #maybe modify this list later to remove certain characters from being chosen
    charid = choice(idlist)
    firstinfo = get_character_stats(charid)
    firststat = firstinfo[whatstat] #Here we can check for errors based on if this value becomes null, which we can aft	er we finish to get rid of the errors that we would get if a character on the superhero api doesn't exist anymore.
    idlist.remove(charid)
    charid = choice(idlist) #Get info from the second character
    secondinfo = get_character_stats(charid)
    secondstat = secondinfo[whatstat]
    packagedinfo = [statname, [firstinfo[0], firstinfo[1], firststat], [secondinfo[0], secondinfo[1], secondstat]]
    return packagedinfo

# For pokeapi

startpokeurl = "https://pokeapi.co/api/v2/pokemon/"

# Returns a list that contains information to be put on the site in the following form:
# [name, imgurl, question, answer] answer will be either a string of the pokemon's name or a list of the pokemon's type(s) as strings.
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
    if qtype == 1: #What is the name of this pokemon?
        question = "What is the name of this pokemon?"
        answer = name
    packagedinfo = [name, img, question, answer]
    return packagedinfo
    
generatepokemonquestion()


#method that gets the stats of a random superhero 
def get_character_stats(character_id): 

  url = f'https://superheroapi.com/api/1016186539784047/{character_id}'
  response = requests.get(url)
  data = response.json()
  info = [data['name'], data['image']['url'], data['powerstats']['intelligence'], data['powerstats']['strength'], data['powerstats']['speed'], data['powerstats']['durability'], data['powerstats']['power'], data['powerstats']['combat']]
  return info


# generatecharacterquestion()



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