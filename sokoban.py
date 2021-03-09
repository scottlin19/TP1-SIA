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
board = Board('maps/medium.txt')
t1_start = perf_counter()
results = algoritm.search(board)
# Stop the stopwatch / counter 
t1_stop = perf_counter()         
print("Elapsed time:", t1_stop, t1_start)
print("Elapsed time during the whole program in ms:", (t1_stop-t1_start)*1000) 
node = results.final_node
steps = []
while node.prev != None:
    print(node)
    print('step: ' + node.direction)
    steps.append(node.direction)
    node = node.prev
print(steps[::-1])

render(results.board.min_and_max[0], results.board.min_and_max[1], results.board.walls, results.board.boxes, results.board.goals, results.board.player, steps[::-1])

