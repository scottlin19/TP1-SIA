#Un nodo tiene solo posiciones, no el board entero.  
#La idea es conseguir todos los nodos hasta que la posicion cada caja coincida con la posicion de algun goal
#El goal siempre va a estar fijo asi que no tiene sentido guardarlo en el nodo. En el nodo me guardo la posicion del player y las cajas
#A partir de un nodo me puedo mover a otros, teniendo en cuenta de no chocarme con paredes ni cajas (para eso esta la funcion get_possible_moves) que basicamente me devuelve los descendientes de ese nodo que es lo mismo que decir los movimientos posibles a partir de esa posicion del player
#Cuando ya tengo los descendientes del nodo, tengo que iterar por cada uno y buscar sus descendientes (breadth first)

from node import Node
from metrics import Metrics
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults
# tree = {} # hash donde la clave es: 'posición del player + posiciones de las cajas' y el valor es lista de nodos


class BFS(SearchMethod):
    # Preguntar si depende de que nodos expandimos primero    
    def search(self,board):
        visited = set()
        queue = []
        node = Node(board.player, board.boxes, None, None)
        metrics = Metrics('bfs',false,0,0,0,0)
        queue.append(node)          #save initial node
        visited.add(node) #save already visited nodes      
        
        while queue:
            
            curr = queue.pop(0)
            if(board.is_completed(curr)):
                metrics.success = true 
                metrics.frontier = len(queue)
                print('finished with: ' + str(metrics.nodes_expanded))
           
                return SearchResults(metrics,curr)
          
            moves = board.get_possible_moves(curr) #get a tree level
            if(moves) #curr has children
                metrics.nodes_expanded += 1
            
            for move in moves:
                if move not in visited:
                   
                    visited.add(move)
                    queue.append(move)
                    
        # Queue is empty so there is no solution 
        metrics.success = false
        return SearchResults(metrics,None)

