from node import Node
from sokoban_render import render
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults
from metrics import Metrics

class IDDFS(SearchMethod):
    def __init(self, limit):
        super().__init__()
        self.limit = limit

    def search(self,board):
        
        node = Node(board.player, board.boxes, None, None)
        metrics = Metrics('IDDFS',False,0,0,0,0)
        stack = []
        visited = set()
        stack.append(node)          #save initial node in stack
        visited.add(node)
        
        while stack:  
            curr = stack.pop() #it is a stack 
            if(board.is_completed(curr)):
                
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