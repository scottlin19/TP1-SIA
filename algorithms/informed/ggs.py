from node import Node
from metrics import Metrics
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults
from algorithms.informed.heuristic import Heuristic

# Se utiliza el Algoritmo de búsqueda genérico, utilizando h(n) como ordenamiento de Fr.

class GGS(SearchMethod):

    def __init__(self, heuristic, checkDeadlocks):
        super().__init__(checkDeadlocks)
        self.heuristic = heuristic
    
    def search(self,board):
        visited = set()
        frontier = []
        node = Node(board.player, board.boxes, None, None, 0, )
        metrics = Metrics('GGS',False,0,0,0,0, 0, [])

        heuristic = Heuristic(board, self.heuristic)

        
        frontier.append(node)       #save initial node
        visited.add(node)           #save already visited nodes 
        
        while frontier:      
            curr = frontier.pop(0)
            
            if board.is_completed(curr):
                return SearchResults(metrics, curr)
            
            moves = board.get_possible_moves(curr, self.checkDeadlocks )
            for move in moves: #save in frontier by h
                if(move not in visited):
                    move.h = heuristic.h(move)
                    visited.add(move)
                    frontier.append(move)
                    if(len(frontier) > 1):
                        frontier = heuristic.sort_nodes(frontier, heuristic.sort_by_h)
                        # hs = [node.h for node in frontier]
                        # print(hs)

        # Frontier is empty so there is no solution 
        metrics.success = False
        return SearchResults(metrics,None)
        
        