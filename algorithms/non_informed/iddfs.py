from node import Node
from sokoban_render import render
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults
from metrics import Metrics

# source: https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/
# Por ahora si no encuentra la solucion corta
# La idea sería : Si no encontro la solucion duplico la profundidad y empiezo a buscar a partir de last_depth 
#                 Si encontró la solución, es la más óptima? Cómo hago para ver eso. Buscar entre last_depth en la que no hubo solución y la depth a la que sí encontré la sn. Y ahí en cuando habría que meter bisección

LIMIT_INCREASE = 10

class IDDFS(SearchMethod):
    def __init__(self, limit, checkDeadlocks):
        super().__init__(checkDeadlocks)
        self.limit = limit
        self.visited = set()
        self.metrics = Metrics('IDDFS',False,0,0,0,0, 0, [])
        self.queue = []
        self.solution_found = False
        self.last_level_nodes = []


    def search(self,board):
        
        node = Node(board.player, board.boxes, None, None, 0)
        
        final_node = self.iddfs(node, board) 
        
        if(final_node is not None):
            self.metrics.success = True 
            self.metrics.frontier = len(self.queue)
            return SearchResults(self.metrics, final_node)
            
        self.metrics.success = False
        return SearchResults(self.metrics, None)
   
    
    def iddfs(self, node, board):
        self.queue.append(node)
        start = 0
        i = 0
        while self.queue:
            while self.queue:
                result = self.iddfs_rec(start, self.limit, board)
                if(result is not None):
                    self.metrics.data.append(start - 10)
                    return result
            start = self.limit
            self.limit += LIMIT_INCREASE
            self.queue = self.last_level_nodes.copy()
            self.last_level_nodes = []
            i += 1
        # NO SOLUTION
        self.metrics.success = False
        return None
    
    def iddfs_rec(self, start, limit, board):
        node = self.queue.pop()
        
        if(board.is_completed(node)): #sn found, now we gotta see if it is optimal
            print(node.depth)
            self.solution_found = True
            # self.queue.append(node)
            print("Encontro la sn") 
            return node

        if(start == limit): #reached max_depth and sn not found
            self.last_level_nodes.insert(0,node)
            return None

        self.visited.add(node)
        self.metrics.nodes_expanded += 1
        
        moves = board.get_possible_moves(node,self.checkDeadlocks)

        for move in moves:
            if(move not in self.visited):
                self.queue.append(move)
                result = self.iddfs_rec(start+1, limit, board)
                if(result is not None):
                    return result
            
        return None