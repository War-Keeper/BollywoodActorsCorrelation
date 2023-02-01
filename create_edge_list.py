import json
import pandas as pd

films = {}

groups = {"links": []}

with open("All_films.json") as films_file:

    file_contents = films_file.read()
    films = json.loads(file_contents)

cols =  ['source', 'target', 'value']
edge_df = pd.DataFrame(columns = cols)

for idx1, x1 in enumerate(films.keys()):
    for idx2, x2 in enumerate(films.keys()):

        if x1 != x2 and idx1 < idx2:
            size = int(len(set(films[x1]) & set(films[x2])))

            if size > 0:
                df = pd.DataFrame([[x1, x2, size]],  columns =  cols)
                edge_df = pd.concat([edge_df, df])

                groups["links"].append({"source":idx1, "target":idx2, "value":size})

edge_df.to_csv("edge_df.csv", index=False)

with open("links.json", "w") as outfile:
    json.dump(groups, outfile)










