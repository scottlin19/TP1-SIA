from node import Node
from metrics import Metrics
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults
from queue import PriorityQueue
import heapq
class A_STAR(SearchMethod):

    def __init__(self, checkDeadlocks):
        super().__init__(checkDeadlocks)        

    def search(self,board):
        visited = set()
        frontier = PriorityQueue()
        node = Node(board.player, board.boxes, None, None, 0)
        metrics = Metrics('A*',False,0,0,0,0, 0, [])
        
        frontier.append(node)       #save initial node
        visited.add(node)           #save already visited nodes 
        while frontier: 
            
            f = cost(curr) + heuristic.apply(curr)
            
            curr = frontier.pop(0)
            
            if board.is_completed(curr):
                return SearchResults(metrics, curr)
            
            moves = board.get_possible_moves(curr)
            for move in moves: #save in frontier order by f. If f is equal then order by increasing h
                visited.append(move)
                frontier.append(move)

        # Frontier is empty so there is no solution 
        metrics.success = False
        return SearchResults(metrics,None)
                        
       
        