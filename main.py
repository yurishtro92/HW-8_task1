import requests

names_list = ['Hulk', 'Captain America', 'Thanos']

def get_max_intelligense_character(names_list):
    intelligence_list = []
    name_and_intelligence = {}
    for name in names_list:
        url = 'https://superheroapi.com/api/2619421814940190/search/' + name
        resp = requests.get(url)
        dict_1 = dict(resp.json())
        for character in dict_1['results']:
            intelligence = int(character['powerstats']['intelligence'])
            intelligence_list.append(intelligence)
            name_and_intelligence[character['name']] = intelligence
    value = max(intelligence_list)
    return print(list(name_and_intelligence.keys())[list(name_and_intelligence.values()).index(value)])

get_max_intelligense_character(names_list)

#

