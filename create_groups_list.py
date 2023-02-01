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

    groups = {"nodes": []}

    for person in people.keys():
        
        for i in people[person]["filmography"]:

            if i["category"] == "actor":

                groups["nodes"].append({"nodeName":people[person]["base"]["name"], "group":1})

                break
            
            if i["category"] == "actress":

                groups["nodes"].append({"nodeName":people[person]["base"]["name"], "group":2})

                break
    
    return groups

owd = os.getcwd()

people = read_json()

groups = get_filmography(people)

print(groups)

os.chdir(owd)

with open("groups.json", "w") as outfile:
    json.dump(groups, outfile)