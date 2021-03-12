from board import Board
import json
from algorithms.bfs import BFS  
from time import perf_counter 
from sokoban_render import render
from algorithms.iddfs import IDDFS  

from algorithms.dfs import DFS 
#Aca parseamos el file de entrada y vamos llamando a cada algoritmo de busqueda

with open("config.json") as f:
    config = json.load(f)
algorithm_list = ['BFS','DFS','IDDFS']
config_algorithm = config.get('algorithm')
algorithm = None
if config_algorithm == None or (config_algorithm not in algorithm_list):
    print("ERROR: No algorithm provided or algorithm not supported. Config must contain an algorithm from the following list: " + str(algorithm_list))
elif config_algorithm == 'BFS':
    print("BFS")
    algorithm = BFS()
elif config_algorithm == 'DFS':
    algorithm = DFS()
elif config_algorithm == 'IDDFS':
    algorithm = IDDFS(2)
    
board = Board('maps/no_solution.txt')

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
render((0,0), board.max_point, board.walls, board.boxes, board.goals, board.player, steps[::-1], results.metrics)

