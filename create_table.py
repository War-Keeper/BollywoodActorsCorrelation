import json
import numpy as np
import pandas as pd

films = {}

with open("All_films.json") as films_file:

    file_contents = films_file.read()

    films = json.loads(file_contents)


shape = (len(films.keys()) , len(films.keys()) ) 

matrix = np.zeros(shape)

for idx1, x1 in enumerate(films.keys()):

    for idx2, x2 in enumerate(films.keys()):

        if x1 != x2:

            matrix[idx1, idx2] = int(len(set(films[x1]) & set(films[x2])))

matrix = (np.rint(matrix)).astype(int)
array_df = pd.DataFrame(data = matrix, 
                        index = films.keys(), 
                        columns = films.keys())

print(array_df)

array_df.to_csv("array_df.csv")











