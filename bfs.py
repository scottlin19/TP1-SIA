#Un nodo tiene solo posiciones, no el board entero.  
#La idea es conseguir todos los nodos hasta que la posicion cada caja coincida con la posicion de algun goal
#El goal siempre va a estar fijo asi que no tiene sentido guardarlo en el nodo. En el nodo me guardo la posicion del player y las cajas
#A partir de un nodo me puedo mover a otros, teniendo en cuenta de no chocarme con paredes ni cajas (para eso esta la funcion get_possible_moves) que basicamente me devuelve los descendientes de ese nodo que es lo mismo que decir los movimientos posibles a partir de esa posicion del player
#Cuando ya tengo los descendientes del nodo, tengo que iterar por cada uno y buscar sus descendientes (breadth first)

from node import Node
from sokoban_render import render

# tree = {} # hash donde la clave es: 'posición del player + posiciones de las cajas' y el valor es lista de nodos

visited = []
queue = []

def bfs(board):

    node = Node(board.player, board.boxes, [])
    queue.append(node)          #save initial node
    visited.append(node)        #save already visited nodes      

    while queue:
        curr = queue.pop(0)
        if(board.is_completed(curr)):
            # tree[curr] = None
            print(curr.steps)
            render(board.min_and_max[0], board.min_and_max[1], board.walls, board.boxes, board.goals, board.player, curr.steps)
            return

        moves = board.get_possible_moves(curr)
        # tree[curr] = moves
        visited.append(curr)
        
        for move in moves:
            if move not in visited:
                visited.append(move)
                queue.append(move)

                
                
 



 