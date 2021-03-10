from node import Node
from sokoban_render import render
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults
from metrics import Metrics

# source: https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/
# Por ahora si no encuentra la solucion corta


class IDDFS(SearchMethod):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit
        self.visited = set()
        self.metrics = Metrics('IDDFS',False,0,0,0,0)


    def search(self,board):
        
        node = Node(board.player, board.boxes, None, None)
        
        final_node = self.iddfs(node, board) 
        
        if(final_node is not None):
            self.metrics.success = True
            return SearchResults(self.metrics, final_node)
            
        self.metrics.success = False
        return SearchResults(self.metrics, final_node)
    
    
    def iddfs(self, node, board):
        for depth in range(self.limit): #Va sumando de a uno la depth y arrancando de cero cada vez. Hay que guardarse last_depth
            print('depth =', depth)
            result = self.iddfs_rec(node, depth, board)
            if(result is not None):
                return result
        return None
    
    
    def iddfs_rec(self, node, depth, board):
        if(board.is_completed(node)):
            print("Encontro la sn") #aca hay que ver si hay una mas optima
            return node

        if(depth <= 0): #Llegue a la max_depth y no encontre sn
            return None

        self.visited.add(node)
        self.metrics.nodes_expanded += 1
        
        moves = board.get_possible_moves(node)

        for move in moves:
            if(move not in self.visited):
                self.visited.add(move)
                result = self.iddfs_rec(move, depth-1, board)
                if(result is not None):
                    return result
                
                self.visited.remove(move) #depth changed
            
        return None
