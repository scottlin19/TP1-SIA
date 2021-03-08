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
        self.player = None
        self.min_and_max = self.fill_board(file)
        # print(min_and_max)

        # moves= self.get_possible_moves(Node(self.player, self.boxes))
        # for m in moves:
        #     print(m)



    def fill_board(self, file):
        lines = [line.strip("\n") for line in file if line != "\n"]
        x = 0
        y = 0
        for line in reversed(lines): # el reversed es para que despues no se renderee al reves el mapa
            x = 0
            for char in line:
                if(char == "#"):
                    self.walls.append((x,y))
                elif char == "^":
                    self.player = (x,y)
                elif char == "o":
                    self.goals.append((x,y))
                elif char == "x":
                    self.boxes.append((x,y))
                x += 1
            y += 1
        return (0,0), (x, y-1)

    def get_possible_moves(self, node):
        moves = [] #moves is an array of Nodes

        #calculate all moves 
        player_left = (node.player[0] - 1, node.player[1])
        player_right = (node.player[0] + 1, node.player[1])
        player_up = (node.player[0], node.player[1] + 1)
        player_down = (node.player[0], node.player[1] - 1)

        self.check_move(moves, node, player_left, LEFT)
        self.check_move(moves, node, player_right, RIGHT)
        self.check_move(moves, node, player_up, UP)
        self.check_move(moves, node, player_down, DOWN)

        return moves

    def check_move(self, moves, node, new_position, direction):
        #check there are no walls around. If there is box check if player can move it
        if(new_position not in self.walls):
            aux = node.steps.copy()
            aux.append(direction)
            if(new_position in node.boxes): #box next to player
                if(self.can_push_box(node.boxes, new_position, direction)): 
                    #hay una box con las mismas coordenadas del player_left --> a esa le tengo que restar x y dejar y igual porque la estoy moviendo a la izq
                    moves.append(Node(new_position, self.get_new_boxes(node.boxes, new_position, direction), aux)) #and player can push it
                #else move is not possible
            else: #there is no wall and no box
                moves.append(Node(new_position, node.boxes, aux))


    def get_new_boxes(self, boxes, player, direction):
        new_boxes = []

        for b in boxes: 

            if(b == player):
                aux = list(b)
                
                if(direction == LEFT):
                    aux[0] = player[0] - 1
                elif(direction == RIGHT):
                    aux[0] = player[0] + 1
                elif(direction == UP):
                    aux[1] = player[1] + 1 
                elif(direction == DOWN):
                    aux[1] = player[1] - 1
                
                b = tuple(aux)

            new_boxes.append(b)



        return new_boxes
    
    def can_push_box(self, boxes, moved_player, direction):
        
        if(direction == LEFT):
            pushed_box = (moved_player[0] -1, moved_player[1])
        elif(direction == RIGHT):
            pushed_box = (moved_player[0] + 1, moved_player[1])
        elif(direction == UP):
            pushed_box = (moved_player[0], moved_player[1] + 1)
        else:  
            pushed_box = (moved_player[0], moved_player[1] - 1)

        if(pushed_box not in self.walls and pushed_box not in boxes):

            if(pushed_box in self.goals):
                return True

            aux_left = (pushed_box[0]-1, pushed_box[1])
            aux_right = (pushed_box[0]+1, pushed_box[1])
            aux_up = (pushed_box[0], pushed_box[1]+1)
            aux_down = (pushed_box[0], pushed_box[1]-1)

            if(aux_up in self.walls or aux_up in boxes or aux_down in self.walls or aux_down in boxes):
                if(aux_left in self.walls or aux_left in boxes or aux_right in self.walls or aux_right in boxes):
                    return False

            return True

        else:
            return False
            
        # return pushed_box not in self.walls and pushed_box not in boxes

    def is_completed(self, node):
        for box in node.boxes:
            if box not in self.goals:
                return False

        return True

    