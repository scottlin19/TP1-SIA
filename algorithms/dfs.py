from node import Node
from sokoban_render import render
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults

# tree = {} # hash donde la clave es: 'posición del player + posiciones de las cajas' y el valor es lista de nodos


class DFS(SearchMethod):
    
    def search(self,board):
        node = Node(board.player, board.boxes, None, None)
        self.queue.append(node)          #save initial node in stack
        self.visited.add(node)
        
        while self.queue:  
            curr = self.queue.pop() #it is a stack 
            if(board.is_completed(curr)):
                # print(curr.steps) 
                print('finished with: ' + str(self.nodes_expanded))
                # render(board.min_and_max[0], board.min_and_max[1], board.walls, board.boxes, board.goals, board.player, curr.steps)
                return SearchResults(board,self.nodes_expanded,curr)
            self.nodes_expanded +=1 
            moves = board.get_possible_moves(curr)
          
            for move in moves:
                if move not in self.visited: 
                    self.queue.append(move)
                    self.visited.add(move)
                    
            
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
        
                    
                    
    
                    
    

            
            