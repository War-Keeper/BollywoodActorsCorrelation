import json
import numpy as np
import pandas as pd

films = {}

with open("All_films.json") as films_file:

    file_contents = films_file.read()

    films = json.loads(file_contents)


shape = (len(films.keys()) , len(films.keys()) ) 

matrix = np.zeros(shape)

matrix2 = [ ['none'] * len(films.keys()) for _ in range(len(films.keys()))]

for idx1, x1 in enumerate(films.keys()):

    for idx2, x2 in enumerate(films.keys()):

        if x1 != x2:
            
            matrix[idx1, idx2] = len(set(list(films[x1].keys())).intersection(list(films[x2].keys())))

            matrix2[idx1][ idx2] = set(list(films[x1].values())) & set(list(films[x2].values()))

matrix = (np.rint(matrix)).astype(int)
array_df = pd.DataFrame(data = matrix, 
                        index = films.keys(), 
                        columns = films.keys())
array_df.style.background_gradient(axis=None)  

array_df2 = pd.DataFrame(data = matrix2, 
                        index = films.keys(), 
                        columns = films.keys())

print(array_df)

array_df.to_csv("array_df.csv")
array_df.to_html("index2.html")
array_df2.to_html("index3.html")




