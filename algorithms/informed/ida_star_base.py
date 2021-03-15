from node import Node
from sokoban_render import render
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults
from metrics import Metrics
from algorithms.informed.heuristic import Heuristic
import math
from time import perf_counter
 
# source: https://es.coursera.org/lecture/resolucion-busqueda/algoritmo-a-con-profundidad-iterada-ida-9bJZe

class IDA_STAR(SearchMethod):
    def __init__(self, heuristic, checkDeadlocks):
        super().__init__(checkDeadlocks)
        self.heuristic = heuristic
        self.visited = set()
        self.metrics = Metrics('IDA*',False,0,0,0,0, 0, [])
        self.stack = []
        self.counter = 0
    
    def search(self,board):

        heuristic = Heuristic(board, self.heuristic)
        
        node = Node(board.player, board.boxes, None, None, 0)
        node.h = heuristic.h(node)

        final_node = self.ida(board, node, heuristic)

        if(final_node is not None):
            self.metrics.success = True 
            self.metrics.frontier = len(self.stack)
            return SearchResults(self.metrics, final_node)
            
        self.metrics.success = False
        return SearchResults(self.metrics, None)

    def ida(self, board, node, heuristic):
        bound = heuristic.h(node) #cost = 0 --> f = h

        while True:
            self.stack.append(node)
            min_cost = math.inf

            while self.stack:
                curr = self.stack[-1] # último elemento de la lista
                print('curr f:', curr.depth + curr.h)
                print('stack:', list(map(lambda x: x.depth + x.h, self.stack)))
                print('\n')
 
                if board.is_completed(curr):
                    self.metrics.success = True
                    return curr

                if curr not in self.visited:
                    self.visited.add(curr)
                    moves = heuristic.sort_nodes(board.get_possible_moves(curr, self.checkDeadlocks), heuristic.sort_by_f)
                    if(moves): #curr has children
                        self.metrics.nodes_expanded += 1
                        
                    for move in moves:
                        move.h = heuristic.h(move)
                        f = move.depth + move.h
                        if f <= bound:
                            if move not in self.visited:
                                self.stack.append(move)
                        else:
                            if f < min_cost:
                                min_cost = f
                else:
                    node_out = self.stack.pop()
                    self.visited.remove(curr)
            
            bound = min_cost
            if bound is math.inf:
                return None
