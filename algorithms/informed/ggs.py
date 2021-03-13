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
                metrics.success = True
                metrics.frontier = len(frontier)
                return SearchResults(metrics, curr)
            
            metrics.nodes_expanded +=1
            moves = board.get_possible_moves(curr, self.checkDeadlocks )
            if(moves): #curr has children
                metrics.nodes_expanded += 1
            for move in moves: #save in frontier by h
                if(move not in visited):
                    move.h = heuristic.h(move)
                    visited.add(move)
                    frontier.append(move)
                    frontier = heuristic.sort_nodes(frontier, heuristic.sort_by_h)

        # Frontier is empty so there is no solution 
        metrics.success = False
        return SearchResults(metrics,None)
        
        