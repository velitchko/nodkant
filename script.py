import os
import json
import networkx as nx

data_directory = './data'

def findCliques(graph):
    cliques = list(nx.enumerate_all_cliques(graph))
    longest_clique = max(cliques, key=len)
    if(len(longest_clique) > 3):
        print(f"Longest clique: {longest_clique}")
    return len(longest_clique) > 3

def contains_fan(graph):
    for node in graph.nodes():
        neighbors = list(graph.neighbors(node))
        if len(neighbors) > 3:  # Assuming "very highly connected" means more than 5 neighbors
            neighbor_count = 0;
            for neighbor in neighbors: 
                if graph.degree(neighbor) == 1:
                    neighbor_count += 1
    
            if neighbor_count > 3:
                return True
    return False

# Get a list of files in the data directory
files = os.listdir(data_directory)

# Iterate over the first 1000 files
for i, file_name in enumerate(files[9001:]):
    file_path = os.path.join(data_directory, file_name)
    if os.path.isfile(file_path):
        # print(f"Processing file {i+1}: {file_name}")
        # Add your file processing code here
        with open(file_path, 'r') as f:
            data = json.load(f)
            graph = nx.node_link_graph(data)
            # cliques_exist = findCliques(graph)
            # if(cliques_exist):
            #     print(f"Cliques exist: {cliques_exist} @ {file_name}")
            fan_exists = contains_fan(graph)
            if(fan_exists):
                print(f"Fan exists: {fan_exists} @ {file_name}")