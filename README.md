# **Bollywood Actors Correlation**

## Checking to see how often 275 of Bollywood's top actors and actresses work together

### Scripted by: Chaitanya Patel, https://www.linkedin.com/in/cpatel3/

#### dataframe 1: https://war-keeper.github.io/BollywoodActorsCorrelation/index2.html
#### dataframe 2: https://war-keeper.github.io/BollywoodActorsCorrelation/index3.html

### Tableau Visualizer: https://public.tableau.com/app/profile/chintu2594/viz/BollywoodActorActressCorrelation/Dashboard1#1
---

### **Note** That the csv and json files that are provided were created on **1/31/2023** using IMDB, if you want to get updated data, please follow the instructions below.



### **If you wish to create your own list of custom names, you can use add/remove the ids from the actorslist.txt and actresslist.txt files**

---


# How to Get Updated Actor/Actress Data:

0. Go to RapidAPI and create your own Key:
https://rapidapi.com/apidojo/api/imdb8

1. After Getting you key, copy it to the **Fetch_all_info.py** (line 10) and hit run. This will create a folder called jsons that will contain all the files for each actor based on their IMDB ID.

    **Note**: This is a free version, so you only get 500 Api requests/Month, There is also a limit on the number of requests per 5 seconds, that is why there is a 5s sleep period between each request.

2. Run **extract_films_lists.py** to extract all the films that the person has been a Actor/Actress or a Producer in. You can change this criteria to all more (ex. Thanks, Soundtrack, Self, etc).

    The File created is already provided, called *All_films.json*

3. You can now use this Data to run either *create_edge_list.py*, or *create_table.py*

    **create_table.py** will create a table that contains the amount of times two people have been in the same Movie/Show together. It will be stored in *array_df.csv*

    **create_edge_list.py** will create create a list of weighted edges for each pair of people that have any movies/shows in common. Two lists are created: 1. The *edge_df.csv* contains the Source, target and value for each pair. The *links.json* contains the same information for is indexed by position of each person (This file is mainly used by index.html for viewing).

    **create_groups_list.py** will create a json for each person and their grouping (Male and Female). This will be used by *index.html* for viewing.

4. After creating the *links.json* and *groups.json*, you have to manually copy them into **Bollywood.js** into their respective places. ( I dont really know JS, so if there is a script that can replace manually copying this over, please let me know). This will be used by **index.html** for viewing.

5. Run *index.html* in a live server. 

---
## Using D3Blocks

- Follow steps 0 to 3 from the above instructions
- Use **create_D3_Blocks.py** to create 3 new html files in D3Blocks.py Folder.
-- NOTE: You may want to change the value for the Weight threshold to show more connections.

---

**Note** that because of the size of the number of actors and the number of connections, it will be SLOW. but you can also just use the array_df.csv for any other purpose or plot it your own way. If you find a better way to plot this, please share it.

**Note 2**: There may be other files in here that are not needed, but I just kept it here just in case you want to use it.
