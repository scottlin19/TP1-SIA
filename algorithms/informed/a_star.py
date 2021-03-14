from node import Node
from metrics import Metrics
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults
from algorithms.informed.heuristic import Heuristic
import bisect



class A_STAR(SearchMethod):

    def __init__(self, heuristic, checkDeadlocks):
        super().__init__(checkDeadlocks)
        self.heuristic = heuristic

    def search(self,board):
        visited = set()
        frontier = []
        node = Node(board.player, board.boxes, None, None, 0)
        metrics = Metrics('A*',False,0,0,0,0, 0, [])

        heuristic = Heuristic(board, self.heuristic)
        
        frontier.append(node)       #save initial node
        visited.add(node)           #save already visited nodes 
        
        
        while frontier: 
            curr = frontier.pop(0)
            
            if board.is_completed(curr):
                metrics.success = True
                metrics.frontier = len(frontier)
                return SearchResults(metrics, curr)
            
            visited.add(curr)
            
            moves = board.get_possible_moves(curr,self.checkDeadlocks)
            if(moves): #curr has children
                metrics.nodes_expanded += 1
            for move in moves: #save in frontier order by f. If f is equal then order by increasing h
                if(move not in visited):
                    move.h = heuristic.h(move)
                    exists = False
                    for node in frontier:
                        if(node.__eq__(move)):
                            exists = True
                            if(node.depth + node.h > move.depth + move.h):
                                frontier.remove(node)
                                bisect.insort(frontier, move)
                    if not exists:
                        bisect.insort(frontier, move)
  
        # Frontier is empty so there is no solution 
        metrics.success = False
        return SearchResults(metrics,None)
                        
       
        