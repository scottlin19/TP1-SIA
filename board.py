#Logica del juego. Tiene todas las posiciones 
from node import Node
from sokoban_render import render

LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'

class Board: 

    def __init__(self, filename):
        file = open(filename, "r")
        self.walls = []
        self.boxes = []
        self.goals = []
        self.player = []
        min_and_max = self.fill_board(file)
        # print(min_and_max)
        render(min_and_max[0], min_and_max[1], self.walls, self.boxes, self.goals, self.player)

        # moves= self.get_possible_moves(Node(self.player, self.boxes))
        # for m in moves:
        #     print(m)


    def fill_board(self, file):
        lines = [line.strip("\n") for line in file if line != "\n"]
        x = 0
        y = 0
        for line in reversed(lines): # el reversed es para que despues no se renderee al reves
            x = 0
            for char in line:
                if(char == "#"):
                    self.walls.append([x,y])
                elif char == "^":
                    self.player.append([x,y])
                elif char == "o":
                    self.goals.append([x,y])
                elif char == "x":
                    self.boxes.append([x,y])
                x += 1
            y += 1
        return [0,0], [x, y-1]

    def get_possible_moves(self, node):
        moves = [] #moves is an array of Nodes

        #calculate all moves 
        player_left = [node.player[0] - 1, node.player[1]]
        player_right = [node.player[0] + 1, node.player[1]]
        player_up = [node.player[0], node.player[1] - 1]
        player_down = [node.player[0], node.player[1] + 1]

        #check there are no walls around. If there is box check if player can move it
        if(player_left not in self.walls):
            if(player_left in node.boxes): #box next to player
                if(self.can_push_box(player_left, LEFT)): 
                    #hay una box con las mismas coordenadas del player_left --> a esa le tengo que restar x y dejar y igual porque la estoy moviendo a la izq
                    moves.append(Node(player_left, self.get_new_boxes(node.boxes, player_left, LEFT))) #and player can push it
                #else move is not possible
            else: #there is no wall and no box
                moves.append(Node(player_left, node.boxes))
                
        if(player_right not in self.walls):
            if(player_right in node.boxes): 
                if(self.can_push_box(player_right, RIGHT)): 
                    moves.append(Node(player_right, self.get_new_boxes(node.boxes, player_right, RIGHT)))  
            else:
                moves.append(Node(player_right, node.boxes))    
            
        if(player_up not in self.walls):
            if(player_up in node.boxes): 
                if(self.can_push_box(player_up, UP)):   
                    moves.append(Node(player_up, self.get_new_boxes(node.boxes, player_up, UP)))
            else: 
                moves.append(Node(player_up, node.boxes))         
                
        if(player_down not in self.walls):
            if(player_down in node.boxes): 
                if(self.can_push_box(player_down, DOWN)): 
                 moves.append(Node(player_down, self.get_new_boxes(node.boxes, player_down, DOWN))) 
            else: 
                moves.append(Node(player_down, node.boxes))

        return moves

    def get_new_boxes(self, boxes, player, direction):
        new_boxes = boxes.copy()
        
        for b in new_boxes: 
            aux = list(b)
            
            if(b == player):
                new_boxes.remove(b)
                 
                if(direction == LEFT):
                    aux[0] = player[0] - 1
                elif(direction == RIGHT):
                    aux[0] = player[0] + 1
                elif(direction == UP):  
                    aux[1] = player[1] - 1 
                elif(direction == DOWN):
                    aux[1] = player[1] + 1    
                     
            b = tuple(aux)
            new_boxes.append(b) 
               
        return new_boxes
    
    def can_push_box(self, moved_player, direction):
        
        if(direction == LEFT):
            pushed_box = [moved_player[0] -1, moved_player[1]]
        elif(direction == RIGHT):
            pushed_box = [moved_player[0] + 1, moved_player[1]]
        elif(direction == UP):
            pushed_box = [moved_player[0], moved_player[1] - 1]
        else:  
            pushed_box = [moved_player[0], moved_player[1] + 1]
            
        return pushed_box not in self.walls and pushed_box not in self.boxes
        

    def append_move(moves, direction, player, boxes): 
        if(player in boxes): #box next to player
            if(can_push_box(player)): 
                #hay una box con las mismas coordenadas del player_left --> a esa le tengo que restar x y dejar y igual porque la estoy moviendo a la izq
                moves.append(Node(player, self.get_new_boxes(boxes, player, direction))) #and player can push it
                #else move is not possible
            else: #there is no wall and no box
                moves.append(Node(player, boxes))


Board('easy.txt')

    