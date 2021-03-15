from node import Node
from sokoban_render import render
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults
from metrics import Metrics
from algorithms.informed.heuristic import Heuristic
import math
 
# source: https://es.coursera.org/lecture/resolucion-busqueda/algoritmo-a-con-profundidad-iterada-ida-9bJZe

class IDA_STAR(SearchMethod):
    def __init__(self, heuristic, checkDeadlocks):
        super().__init__(checkDeadlocks)
        self.heuristic = heuristic
        self.limit = 0
        self.visited = set()
        self.metrics = Metrics('IDA*',False,0,0,0,0, 0, [])
        self.queue = []
        self.solution_found = False


    def search(self,board):
        
        heuristic = Heuristic(board, self.heuristic)
        node = Node(board.player, board.boxes, None, None, 0)
        self.limit =  heuristic.h(node) #cost is 0 --> F = H
        final_node = self.iddfs(node, board, heuristic) 
        
        if(final_node is not None):
            self.metrics.success = True 
            self.metrics.frontier = len(self.queue)
            return SearchResults(self.metrics, final_node)
            
        self.metrics.success = False
        return SearchResults(self.metrics, None)
   
    
    def iddfs(self, node, board, heuristic):
        self.queue.append(node)
        start = 0

        result = self.iddfs_rec(self.queue.pop(0), start, self.limit, board)
        if(result is not None):
            return result
        else: #no encontré sn, vuelvo a empezar con limit = min_f
            start = 0
            min_f = math.inf

            while len(self.queue) > 0:
                result = self.iddfs_rec(self.queue.pop(0), start, self.limit, board)
                
                if(result is not None):
                    return result
             
                for node in self.queue:
                    f = node.depth + heuristic.h(node)
                    if f < min_f: 
                        min_f = f
                self.limit = min_f
                

        # NO SOLUTION
        self.metrics.success = False
        return None


    def iddfs_rec(self, node, start, limit, board):
        
        if(board.is_completed(node)): #sn found
            self.solution_found = True
            return node

        if(start == limit): #reached max_depth and sn not found
            self.queue.append(node)
            return None

        self.visited.add(node)
        self.metrics.nodes_expanded += 1
        
        moves = board.get_possible_moves(node)

        for move in moves:
            if(move not in self.visited):
                self.visited.add(move)
                result = self.iddfs_rec(move, start+1, limit, board)
                if(result is not None):
                    return result
            
        return None



