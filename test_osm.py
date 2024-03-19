#pip install osmnx


# import osmnx as ox
# import matplotlib.pyplot as plt

# # Specify the location and name of the place you're interested in
# place_name = "Vestland, Norway"

# # Configure osmnx to retrieve only road network data for drivable roads
# ox.config(use_cache=True, log_console=True)

# # Retrieve the road network for the specified place, focusing on drivable roads
# graph = ox.graph_from_place(place_name, network_type='drive')

# # Plot the road network
# fig, ax = ox.plot_graph(ox.project_graph(graph))

# plt.show()

import osmnx as ox
import matplotlib.pyplot as plt

# Configuration for osmnx
ox.config(use_cache=True, log_console=True)

# Area of interest
place_name = "Vestland, Norway"

# Download street network for cars
G = ox.graph_from_place(place_name, network_type='drive')

# Project the graph for better visualization
G_proj = ox.project_graph(G)

# idea:
#     'Road Name not really used   # 0-20%: Green
#     'Road Name used somewhat  # 21-40%: Yellow
#     'Road Name moderately used  # 41-60%: Orange
#     'Road Name often used  # 61-80%: Red
#     'Road Name very often used   # 81-100%: Very dark red

# Function to get color based on percentage TODO: change to number/volum
def get_color(percentage):
    if percentage <= 20: 
        return 'green'
    elif percentage <= 40:
        return 'yellow'
    elif percentage <= 60:
        return 'orange'
    elif percentage <= 80:
        return 'red'
    else:
        return '#8B0000'  # Dark red

# Initialize a list to hold the colors for each edge
ec = []

# Loop through each edge in the graph
for u, v, key, data in G_proj.edges(keys=True, data=True):
    # Default color
    color = 'grey'  # Roads not in the list
    # Check if this road has a name and is in our interest list
    if 'name' in data and data['name'] in road_percentages:
        # Get the percentage increase for this road
        percentage = road_percentages[data['name']]
        # Determine the color based on the percentage
        color = get_color(percentage)
    # Append the color to the list
    ec.append(color)

# Plot the graph with customized edge colors
fig, ax = ox.plot_graph(G_proj, bgcolor='k', edge_color=ec, edge_linewidth=1.5, node_size=0)
plt.show()
