# --
# Day 8: Playground
# --
import math
from itertools import combinations

import networkx as nx
import numpy as np

# Part 1
points = []
with open("Input/day8_input.txt") as input:
    for line in input:
        coords = [int(x.strip()) for x in line.split(",")]
        points.append(coords)


def calc_euclidean_distance(point1, point2):
    """Calculates the euclidean distance between two points in three dimensional space.
    args:
        point1 (list): coordinates of point 1 (x,y,z)
        point2 (list) coordinates of point 2 (x,y,z)
    returns:
        float: euclidean distance between the two points"""

    point1 = np.array(point1)
    point2 = np.array(point2)

    return np.linalg.norm(point1 - point2)


edges = []
# calculate all euclidean distances between every point
for i, j in combinations(range(len(points)), 2):
    distance = calc_euclidean_distance(points[i], points[j])
    edges.append((distance, i, j))

edges.sort(key=lambda x: x[0])  # shortest distance first
# print(edges)
# "after making the 1000 shortest connections" - so plot the 1000 shortest edges using NetworkX
edges_idx = [(i, j) for _, i, j in edges[:1000]]

G = nx.Graph()
G.add_edges_from(edges_idx)

# the three largest circuits are then the 3 largest connected "clusters" in this graph
largest_circuits = [
    len(circuit)
    for circuit in sorted(nx.connected_components(G), key=len, reverse=True)
]
#print(largest_circuits)
print(f"The sum of three largest circuits is: {math.prod(largest_circuits[:3])}")

# Part 2:

# What are the last two nodes I need to add to have every node connected be in a singular loop?
G = nx.Graph()
G.add_nodes_from(range(len(points)))

last_edge = None
for distance, i, j in edges:  # edges are already sorted by distance
    G.add_edge(i, j)
    if nx.is_connected(G):  # keep adding edges until every node is connected
        last_edge = (i, j)
        break

if last_edge is not None:
    i, j = last_edge
    x_product = points[i][0] * points[j][0]  # multiply x-components
    print(f"Last edge nodes: {points[i]}, {points[j]}")
    print(f"Product of x-components: {x_product}")
