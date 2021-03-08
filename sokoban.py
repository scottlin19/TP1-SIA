from board import Board
import json
from algorithms.bfs import BFS  
#Aca parseamos el file de entrada y vamos llamando a cada algoritmo de busqueda

with open("config.json") as f:
    config = json.load(f)
algorithm_list = ['BFS','DFS','IDDFS']
if config.get('algorithm') == None or (config.get('algorithm') not in algorithm_list):
    print("ERROR: No algorithm provided or algorithm not supported. Config must contain an algorithm from the following list: [\"BFS\",\"DFS\",\"IDDFS\"]")
else:
    board = Board('map.txt')
    
    bfs = BFS()
    bfs.search(board)