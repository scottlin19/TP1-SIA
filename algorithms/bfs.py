#Un nodo tiene solo posiciones, no el board entero.  
#La idea es conseguir todos los nodos hasta que la posicion cada caja coincida con la posicion de algun goal
#El goal siempre va a estar fijo asi que no tiene sentido guardarlo en el nodo. En el nodo me guardo la posicion del player y las cajas
#A partir de un nodo me puedo mover a otros, teniendo en cuenta de no chocarme con paredes ni cajas (para eso esta la funcion get_possible_moves) que basicamente me devuelve los descendientes de ese nodo que es lo mismo que decir los movimientos posibles a partir de esa posicion del player
#Cuando ya tengo los descendientes del nodo, tengo que iterar por cada uno y buscar sus descendientes (breadth first)

from node import Node
from sokoban_render import render
from algorithms.searchMethod import SearchMethod
# tree = {} # hash donde la clave es: 'posición del player + posiciones de las cajas' y el valor es lista de nodos


class BFS(SearchMethod):
    
    def search(self,board):
        node = Node(board.player, board.boxes, [])
        self.queue.append(node)          #save initial node
        self.visited.append(node)        #save already visited nodes      
        while self.queue:
            curr = self.queue.pop(0)
            if(board.is_completed(curr)):
                # tree[curr] = None
                print(curr.steps)
                render(board.min_and_max[0], board.min_and_max[1], board.walls, board.boxes, board.goals, board.player, curr.steps)
                return

            moves = board.get_possible_moves(curr)
            # tree[curr] = moves
            self.visited.append(curr)
            self.nodes_expanded +=1 
            for move in moves:
                if move not in self.visited:
                    self.visited.append(move)
                    self.queue.append(move)

