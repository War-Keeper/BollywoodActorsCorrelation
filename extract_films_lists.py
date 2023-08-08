import json
import os

def read_json():

    people = {}

    path = "jsons/"

    os.chdir(path)

    # iterate through all files
    for file in os.listdir():

        with open(file) as user_file:

            file_contents = user_file.read()

            jsn = json.loads(file_contents)

            people[jsn["base"]["name"]] = jsn

    return people

def get_filmography(people):

    films = {}

    for person in people.keys():

        films[person] = {}


        for i in people[person]["filmography"]:
            # print(i["category"])
            # print(i["id"][7:-1])

            if i["category"] == "actor" or i["category"] == "producer" or i["category"] == "actress":
                if i["titleType"] == "movie" or i["titleType"] == "tvSeries" or i["titleType"] == "tvEpisode":

                    films[person][i["id"][7:-1]] = i["title"]


    return films

owd = os.getcwd()

people = read_json()

films = get_filmography(people)

os.chdir(owd)

with open("All_films.json", "w") as outfile:
    json.dump(films, outfile)

# print(list(films["Amitabh Bachchan"].keys()))

# print name
# print(people["nm0000821"]["base"]["name"])

# list of filmography
# print(people["nm0000821"]["filmography"]

# first one in filmography
# print(people["nm0000821"]["filmography"][0])







