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
#Aca parseamos el file de entrada y vamos llamando a cada algoritmo de busqueda

with open("config.json") as f:
    config = json.load(f)
algorithm_list = ['BFS','DFS','IDDFS', 'GGS']
config_algorithm = config.get('algorithm')
config_heuristic = config.get('heuristic')
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
    algorithm = A_STAR(checkDeadlocks)
elif config_algorithm == 'GGS':
    algorithm = GGS(config_heuristic, checkDeadlocks)
elif config_algorithm == 'IDA*':
    algorithm = IDA_STAR(checkDeadlocks)
    
board = Board('maps/easy.txt')

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
results.metrics.cost = depth
render((0,0), board.max_point, board.walls, board.boxes, board.goals, board.player, steps[::-1], results.metrics)

