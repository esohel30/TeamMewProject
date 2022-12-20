import requests
from random import randint, choice
from get_api_key import get_key

'''
Pokemon id list gotten from:

pokeidlist = []
for i in range(1,907):
    try:
        pokeurl = startpokeurl + (str)(i)
        req = requests.get(pokeurl)
        info = req.json()
        name = info['forms'][0]['name']
        if "-" not in name:
            pokeidlist += [i]
    except:
        pass
print(pokeidlist)
'''

'''
Character idlist gotten from:

charidlist = []
for i in range(1,732):
    if "null" not in get_character_stats(i):
        charidlist += [i]
print(charidlist)
'''

with open("idlists.txt") as f:
    pokeidlist = f.readline().rstrip().split(", ")
    charidlist = f.readline().rstrip().split(", ")
    
startpokeurl = "https://pokeapi.co/api/v2/pokemon/"
    
#method that gets the stats of a random superhero 
def get_character_stats(character_id): 
    key = get_key()
    url = f'https://superheroapi.com/api/{key}/{character_id}'
    response = requests.get(url)
    data = response.json()
    info = [data['name'], data['image']['url'], data['powerstats']['intelligence'], data['powerstats']['strength'], data['powerstats']['speed'], data['powerstats']['durability'], data['powerstats']['power'], data['powerstats']['combat']]
    return info

# Returns a list that contains information to be put on the site in the following form:
# [statname, [char1name, char1imgurl, char1stat], [char2name, char2imgurl, char2stat]]
def generatecharacterquestion():
    statlist = ["intelligence", "strength", "speed", "durability", "power", "combat"]
    whatstat = randint(2,7)
    statname = statlist[(whatstat - 2)] # The stat that is being compared
    idlist = charidlist #maybe modify this list later to remove certain characters from being chosen
    charid = int(choice(idlist))
    firstinfo = get_character_stats(charid)
    firststat = firstinfo[whatstat] #Here we can check for errors based on if this value becomes null, which we can after we finish to get rid of the errors that we would get if a character on the superhero api doesn't exist anymore.
    idlist.remove(str(charid))
    charid = int(choice(idlist)) #Get info from the second character
    secondinfo = get_character_stats(charid)
    secondstat = secondinfo[whatstat]
    packagedinfo = [statname, [firstinfo[0], firstinfo[1], firststat], [secondinfo[0], secondinfo[1], secondstat]]
    return packagedinfo

# For pokeapi

# Returns a list that contains information to be put on the site in the following form:
# [name, imgurl, question, answer] answer will be either a string of the pokemon's name or a list of the pokemon's type(s) as strings.
def generatepokemonquestion(): #Some pokemon names will have a "-" in the name, we should let the user get the question correct even if they don't include the "-" or anything past it.
    pokeid = choice(pokeidlist)
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
    if qtype == 1: #Who's that pokemon?
        question = "Who's that pokemon?"
        answer = name
    packagedinfo = [img, question, answer]
    return packagedinfo

def get_yes_no_gif(is_yes):
    '''takes boolean is_yes and returns url of gif'''
    if is_yes:
        query = 'yes'
    else:
        query = 'no'
    url = f'https://yesno.wtf/api?force={query}'
    req = requests.get(url)
    info = req.json()
    gif_url = info['image']
    if gif_url == 'https://yesno.wtf/assets/no/3-80a6f5b5d6684674bcfeda34accca4e1.gif':
        return get_yes_no_gif(is_yes)
    return gif_url


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

if __name__ == '__main__':
    print(get_yes_no_gif(True))
    print(get_yes_no_gif(False))