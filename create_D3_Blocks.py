#############################
# You can check example outputs in the D3Blocks folder
#############################

# Make sure to pip install d3blocks   
from d3blocks import D3Blocks
import pandas as pd
#
# Initialize
d3 = D3Blocks()

# threshold for performance. lowering this will decrease performance and also clutter the charts
threshold = 10


# Read in the edgelist from the csv
df = pd.read_csv("edge_df.csv")

# change the column name from value to weight
df = df.rename(columns={"value": "weight"})

# Because of the shear amount of links, we will only look at values greater than threshold
df = df[df["weight"] > threshold]

# to create a Chord Diagram
# https://d3blocks.github.io/d3blocks/pages/html/Chord.html
d3.chord(df, filepath='D3Blocks/D3chord_' + str(threshold) + '+.html')

# to create a Dynamic Network Graph
# https://erdogant.github.io/d3graph/pages/html/index.html
d3.d3graph(df, filepath='D3Blocks/D3graph_' + str(threshold) + '+.html')

# Convert Vectors to Adjacency Matrix
df = d3.vec2adjmat(df['source'], df['target'], weight=df['weight'], symmetric=True)
#
# to create a Heat map
# https://d3blocks.github.io/d3blocks/pages/html/Heatmap.html
d3.heatmap(df, filepath='D3Blocks/D3heatmap_' + str(threshold) + '+.html')

