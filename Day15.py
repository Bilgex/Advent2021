
from copy import deepcopy

import numpy as np
import pandas as pd
from heapq import *

df = pd.read_table("Day15.txt",header=None,dtype=str)
danger_map=[]
for row in df[0]:
    danger_map.append([int(s) for s in row])
danger_map=np.array(danger_map)
map_size=danger_map.shape[0]

def find_neighbor(coord,size=map_size):
    neighbor_list = {
        (coord[0] + 1, coord[1]),
        (coord[0], coord[1] + 1),
        (coord[0], coord[1] - 1),
        (coord[0] - 1, coord[1]),
        
    }
    neighbors=set()
    for n in neighbor_list:
        if size-1>=n[0]>=0 and size-1>=n[1]>=0:
            neighbors.add(n)
    return neighbors
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]
def part1():
    # Initialize
    choosen=(0,(0,0))
    visited=set()
    seen={(0,0)}
    shortests=[]
    heapify(shortests)
    unvisited={}
    #Do stuff
    while choosen[1]!=(map_size-1,map_size-1):
        if choosen[1] not in visited:
            comparisons=find_neighbor(choosen[1],size=map_size).difference(visited)
            visited.add(choosen[1])
            for neighbor in comparisons:
                if neighbor not in seen:
                    heappush(shortests,(choosen[0]+danger_map[neighbor],neighbor))
                    unvisited[neighbor]=choosen[0]+danger_map[neighbor]
                    seen.add(neighbor)
                elif choosen[0]+danger_map[neighbor]<unvisited[neighbor]:
                    unvisited[neighbor]=choosen[0]+danger_map[neighbor]
                    heappush(shortests,(unvisited[neighbor],neighbor))
        choosen=heappop(shortests)
    return choosen


map_0=deepcopy(danger_map)
for i in range(1,5):
    map_i=map_0+i
    map_i[map_i>9]-=9
    danger_map=np.concatenate((danger_map,map_i),axis=1)
map_0=deepcopy(danger_map)
for i in range(1,5):
    map_i=map_0+i
    map_i[map_i>9]-=9
    danger_map=np.concatenate((danger_map,map_i),axis=0)
map_size=danger_map.shape[0]
print(part1())
    

        


   




"""
unvisited_nodes=set()
def def_value():
    return 10000
visit_costs=defaultdict(None)
for i in range(map_size):
    for j in range(map_size):
        unvisited_nodes.add((i,j))
visit_costs[(0,0)]=0
def walker(position=(0,0)):
    neighbors=find_neighbor(position)
    unvisited_nodes.remove(position)
    if len(unvisited_nodes)==0:
        return visit_costs
    for neighbor in neighbors:
        if neighbor in unvisited_nodes:
            if visit_costs[neighbor]>danger_map[neighbor]+visit_costs[position]:
                visit_costs[neighbor]=danger_map[neighbor]+visit_costs[position]
    min_cost=10000
    selected="Not Found"
    for neighbor in neighbors:
        if visit_costs[neighbor]<min_cost and neighbor in unvisited_nodes:
            min_cost=visit_costs[neighbor]
            selected=neighbor
    if selected!="Not Found":
        return walker(selected)
    min_cost<10000
    for node in unvisited_nodes:
        if visit_costs[node]<min_cost:
            if visit_costs[node]<min_cost:
                min_cost=visit_costs[node]
                selected=node
    return walker(selected)
    
            
    """
"""        
position=(0,0)
while len(unvisited_nodes)>0:
    if position in unvisited_nodes:
        unvisited_nodes.remove(position)
        neighbors=find_neighbor(position)
        for n in neighbors:
            cost=danger_map[n]
            if cost==None:
                visit_costs[n]=cost
            else:
                if cost<visit_costs[n]:
"""
