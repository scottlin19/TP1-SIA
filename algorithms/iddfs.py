from node import Node
from sokoban_render import render
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults
from metrics import Metrics

# source: https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/
# Por ahora si no encuentra la solucion corta
# La idea sería : Si no encontro la solucion duplico la profundidad y empiezo a buscar a partir de last_depth 
#                 Si encontró la solución, es la más óptima? Cómo hago para ver eso. Buscar entre last_depth en la que no hubo solución y la depth a la que sí encontré la sn. Y ahí en cuando habría que meter bisección

class IDDFS(SearchMethod):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit
        self.visited = set()
        self.metrics = Metrics('IDDFS',False,0,0,0,0)
        self.queue = []
        self.solution_found = False


    def search(self,board):
        
        node = Node(board.player, board.boxes, None, None, 0)
        
        final_node = self.iddfs(node, board) 
        
        if(final_node is not None):
            self.metrics.success = True
            return SearchResults(self.metrics, final_node)
            
        self.metrics.success = False
        return SearchResults(self.metrics, final_node)
    
    
    def iddfs(self, node, board):
        self.queue.append(node)
        start = 0

        result = self.iddfs_rec(self.queue.pop(0), start, self.limit, board)
        if(result is not None):
            return result
        else:
            queue_len = len(self.queue)
            aux_len = 1
            start = self.limit
            self.limit *= 2

            while True:
                result = self.iddfs_rec(self.queue.pop(0), start, self.limit, board)
                # if(result is not None):
                #     return result

                if(aux_len >= queue_len):
                    
                    if(self.solution_found): #Search optimal sn: in queue there are nodes of different levels, we gotta see which node is sn and has the mininum level
                        optimal_solution = None
                        for node in self.visited:
                            if(board.is_completed(node)):
                                print(node)
                        print('--------------')
                        for node in self.queue:
                            if(board.is_completed(node)):
                                print(node)
                                if(optimal_solution is None or node.depth < optimal_solution.depth):
                                    optimal_solution = node
                        return optimal_solution

                                
                    #Solution not found, so we gotta duplicate limit and we start searching from last_depth (limit)
                    start = self.limit
                    self.limit *= 2
                    aux_len = 1
                    queue_len = len(self.queue)
                else:
                    aux_len += 1


    
    
    def iddfs_rec(self, node, start, limit, board):
        
        if(board.is_completed(node)): #sn found, now we gotta see if it is optimal
            self.solution_found = True
            self.queue.append(node)
            print("Encontro la sn") 
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
                self.visited.remove(move)
            
        return None
