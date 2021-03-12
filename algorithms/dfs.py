from node import Node
from sokoban_render import render
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults
from metrics import Metrics
# tree = {} # hash donde la clave es: 'posición del player + posiciones de las cajas' y el valor es lista de nodos


class DFS(SearchMethod):
    
    def search(self,board):
        node = Node(board.player, board.boxes, None, None)
        metrics = Metrics('DFS',False,0,0,0,0, 0, [])
        stack = []
        visited = set()
        stack.append(node)          #save initial node in stack
        visited.add(node)
        
        while stack:  
            curr = stack.pop() #it is a stack 
            if(board.is_completed(curr)):
                metrics.success = True
                metrics.frontier = len(stack)
                print('finished with: ' + str(metrics.nodes_expanded))
                return SearchResults(metrics,curr)
             
            moves = board.get_possible_moves(curr)
          
            for move in moves:
                if move not in visited: 
                    stack.append(move)
                    visited.add(move)
                    
        # Stack is empty so there is no solution 
        metrics.success = False
        return SearchResults(metrics,None)
                    
            
    """ def search(self, board): 
        node = Node(board.player, board.boxes, [])
        visited = self.searchRec(board, node, self.visited)   
        print(visited)            

    def searchRec(self, board, node, visited): 
        if node not in self.visited: 
            self.visited.append(node)
            
            moves = board.get_possible_moves(node)
            for move in moves:
                searchRec(self, board, move, visited)
        return visited  """            
        
                    
                    
    
                    
    

            
            