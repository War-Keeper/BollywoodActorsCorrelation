import requests
import json
import time
import os

url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography"

# querystring = {"nconst":"nm0474774"}

headers = {
	"X-RapidAPI-Key": "xxxxxx",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

path = './jsons'

# create new single directory
os.mkdir(path)


actors = 0
with open('actorslist.txt') as f:
    actors = f.read().splitlines() 

for i in actors:

    querystring = {"nconst":i}

    response = requests.request("GET", url, headers=headers, params=querystring)

    response = response.json()

    # Serializing json
    json_object = json.dumps(response, indent=4)
    
    # Writing to file
    name = 'jsons/' + i + '.json'
    with open(name, "w") as outfile:
        outfile.write(json_object)
    
    time.sleep(5)



actresses = 0
with open('actresslist.txt') as f:
    actresses = f.read().splitlines() 

for i in actresses:

    querystring = {"nconst":i}

    response = requests.request("GET", url, headers=headers, params=querystring)

    response = response.json()

    # Serializing json
    json_object = json.dumps(response, indent=4)
    
    # Writing to file
    name = 'jsons/' + i + '.json'
    with open(name, "w") as outfile:
        outfile.write(json_object)

    time.sleep(5)
