from board import Board
import json
from time import perf_counter 
from sokoban_render import render

#Search methods
from algorithms.non_informed.bfs import BFS  
from algorithms.non_informed.iddfs import IDDFS  
from algorithms.non_informed.dfs import DFS 
from algorithms.informed.ggs import GGS
from algorithms.informed.a_star import A_STAR
from algorithms.informed.ida_star import IDA_STAR
#Aca parseamos el file de entrada y vamos llamando a cada algoritmo de busqueda

with open("config.json") as f:
    config = json.load(f)
algorithm_list = ['BFS','DFS','IDDFS', 'GGS', 'A*', 'IDA*']
config_algorithm = config.get('algorithm')
config_heuristic = config.get('heuristic')
config_map = config.get('map')
checkDeadlocks = config.get('checkDeadlocks')

algorithm = None
if config_algorithm == None or (config_algorithm not in algorithm_list):
    print("ERROR: No algorithm provided or algorithm not supported. Config must contain an algorithm from the following list: " + str(algorithm_list))
elif config_algorithm == 'BFS':
    print("BFS")
    algorithm = BFS(checkDeadlocks)
elif config_algorithm == 'DFS':
    algorithm = DFS(checkDeadlocks)
elif config_algorithm == 'IDDFS':
    algorithm = IDDFS(2, checkDeadlocks)
elif config_algorithm == 'A*':
    algorithm = A_STAR(config_heuristic, checkDeadlocks)
elif config_algorithm == 'GGS':
    algorithm = GGS(config_heuristic, checkDeadlocks)
elif config_algorithm == 'IDA*':
    algorithm = IDA_STAR(config_heuristic, checkDeadlocks)
    
board = Board(config_map)

t1_start = perf_counter()
results = algorithm.search(board)
# Stop the stopwatch / counter 
t1_stop = perf_counter()         
print("Elapsed time:", t1_stop, t1_start)
print("Elapsed time during the whole program in ms:", (t1_stop-t1_start)*1000) 

node = results.final_node
print(node)
steps = []
depth = 0

while node is not None and node.prev is not None:
    depth += 1
    steps.append(node.direction)
    node = node.prev



#With A* check if the heuristic is consistent => heuristic is admissible
consistent = True 
node = results.final_node
if(node.h != 0):
    consistent = False
while node is not None and node.prev is not None:
    if(node.prev.h > 1 + node.h ):
        consistent = False 
    node = node.prev

    
#Another way to check if is admissble
OPTIMAL_SN = 78
admissible = True 
node = results.final_node
while node is not None and node.prev is not None:
    if(node.h > OPTIMAL_SN - node.depth ): #for soko1   h(n)
        admissible = False 
    node = node.prev   
        
print("consistent: %r" %consistent)    
print("admissible: %r" %admissible)     
print(steps[::-1])
print(len(steps))
print("depth: %d" %depth)
print("params: " + results.metrics.params)
print("success %r" %results.metrics.success)
print("nodes expanded %d" %results.metrics.nodes_expanded)
print("nodes in frontier %d" %results.metrics.frontier)
print("cost %d " %results.metrics.cost)
results.metrics.time = (t1_stop-t1_start)*1000
results.metrics.depth = depth
results.metrics.cost = depth
render((0,0), board.max_point, board.walls, board.boxes, board.goals, board.player, steps[::-1], results.metrics)


def heuristic_is_consistent( node):
    
    if(node.h != 0): #If it is consistent h(goal) = 0
        return False
    
    while node is not None and node.prev is not None:
        if(node.prev.h > 1 + node.h ): #as they are neighbours, if it's consistent h(ni) <= cost(ni, nj) + h(nj)
            return False
        node = node.prev
    
    return True 


def heuristic_is_admissible(node):
    OPTIMAL_SN = 78 #for soko1
    
    while node is not None and node.prev is not None:
        if(node.h > OPTIMAL_SN - node.depth ): #if it is admissible h(n) <= h*(n)
            return False
        node = node.prev  
    
    return True