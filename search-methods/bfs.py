#Un nodo tiene solo posiciones, no el board entero. if tengo espacio  node.player_pos = move(left) --> move crea un nuevo nodo, if la nueva pos que me dio coincide con la de la caja, aumenta la pos de la caja
from node import Node

    def bfs(board):
        visited = []
        queue = []

        node = Node(board.player, board.boxes)
        queue.append(node)          #save initial node
        visited.append(node)        

        #while queue:
            curr = queue.pop(0)
            moves = board.get_possible_moves(node)
 



 