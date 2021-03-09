from board import Board
import json
from algorithms.bfs import BFS  
from time import perf_counter 
from sokoban_render import render

from algorithms.dfs import DFS 
#Aca parseamos el file de entrada y vamos llamando a cada algoritmo de busqueda

with open("config.json") as f:
    config = json.load(f)
algorithm_list = ['BFS','DFS','IDDFS']
config_algoritm = config.get('algorithm')

if config_algoritm == None or (config_algoritm not in algorithm_list):
    print("ERROR: No algorithm provided or algorithm not supported. Config must contain an algorithm from the following list: " + str(algorithm_list))
elif config_algoritm == 'BFS':
    print("BFS")
    algoritm = BFS()
elif config_algoritm == 'DFS':
    algoritm = DFS()
    
board = Board('maps/soko1.txt')

t1_start = perf_counter()
results = algoritm.search(board)
# Stop the stopwatch / counter 
t1_stop = perf_counter()         
print("Elapsed time:", t1_stop, t1_start)
print("Elapsed time during the whole program in ms:", (t1_stop-t1_start)*1000) 

node = results.final_node
steps = []
depth = 0
while node != None and node.prev != None:
    print(node)
    print('step: ' + node.direction)
    depth += 1
    steps.append(node.direction)
    node = node.prev
print(steps[::-1])
print(len(steps))
print("depth: " + depth)
print("params: " + results.metrics.params)
print("success " + results.metrics.success)
print("nodes expanded " + results.metrics.nodes_expanded)
print("nodes in frontier " + results.metrics.frontier)
print("cost " + results.metrics.cost)
render(board.min_and_max[0], board.min_and_max[1], board.walls, results.final_node.boxes, board.goals, results.final_node.player, steps[::-1])

