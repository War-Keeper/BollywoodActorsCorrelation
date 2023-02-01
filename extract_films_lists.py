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

            people[file[:-5]] = json.loads(file_contents)

    return people

def get_filmography(people):

    films = {}

    for person in people.keys():

        films[people[person]["base"]["name"]] = []

        for i in people[person]["filmography"]:
            # print(i["category"])
            # print(i["id"][7:-1])

            if i["category"] == "actor" or i["category"] == "producer" or i["category"] == "actress":
                films[people[person]["base"]["name"]].append(i["id"][7:-1])


    return films

owd = os.getcwd()

people = read_json()

films = get_filmography(people)

os.chdir(owd)

with open("All_films.json", "w") as outfile:
    json.dump(films, outfile)

# print name
# print(people["nm0000821"]["base"]["name"])

# list of filmography
# print(people["nm0000821"]["filmography"]

# first one in filmography
# print(people["nm0000821"]["filmography"][0])







