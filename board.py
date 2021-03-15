#Logica del juego. Tiene todas las posiciones 
from node import Node
from sokoban_render import render
from invalidMapException import InvalidMapException

LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'

class Board: 

    def __init__(self, filename):
        file = open(filename, "r")
        self.walls = set()
        self.boxes = set()
        self.goals = set()
        self.player = None
        self.max_point = self.fill_board(file)
        # print(min_and_max)

        # moves= self.get_possible_moves(Node(self.player, self.boxes))
        # for m in moves:
        #     print(m)



    def fill_board(self, file):
        lines = [line.strip("\n") for line in file if line != "\n"]
        x = 0
        y = 0
        max_x = 0
        for line in reversed(lines): # el reversed es para que despues no se renderee al reves el mapa
            x = 0
            for char in line:
                if(char == "#"):
                    self.walls.add((x,y))
                elif char == "^":
                    self.player = (x,y)
                elif char == "o":
                    self.goals.add((x,y))
                elif char == "x":
                    self.boxes.add((x,y))
                elif char == "%":
                    self.boxes.add((x,y))
                    self.goals.add((x,y))
                elif char == "$":
                    self.player = (x,y)
                    self.goals.add((x,y))

                x += 1
                if(x > max_x):
                    max_x = x
            y += 1
        if(len(self.boxes) == 0 or len(self.goals) == 0): raise InvalidMapException("ERROR: Map must have at least one box and goal")
        elif(len(self.boxes) != len(self.goals)): raise InvalidMapException("ERROR: Map must have same amount of boxes and goals")
        return (max_x-1, y-1)

    def get_possible_moves(self, node, checkDeadlocks):
        moves = [] #moves is an array of Nodes

        #calculate all moves 
        player_left = (node.player[0] - 1, node.player[1])
        player_right = (node.player[0] + 1, node.player[1])
        player_up = (node.player[0], node.player[1] + 1)
        player_down = (node.player[0], node.player[1] - 1)

        self.check_move(moves, node, player_left, LEFT, checkDeadlocks)
        self.check_move(moves, node, player_right, RIGHT, checkDeadlocks)
        self.check_move(moves, node, player_up, UP, checkDeadlocks)
        self.check_move(moves, node, player_down, DOWN, checkDeadlocks)

        return moves

    def check_move(self, moves, node, new_position, direction, checkDeadlocks):
        #check there are no walls around. If there is box check if player can move it
        if(new_position not in self.walls):
            
            if(new_position in node.boxes): #box next to player
                boxes_copy = node.boxes.copy()
                boxes_copy.remove(new_position)
                if(self.can_push_box(boxes_copy, new_position, direction, checkDeadlocks)): 
                    moves.append(Node(new_position, self.get_new_boxes(node.boxes, new_position, direction), node,direction, node.depth + 1)) #and player can push it
                #else move is not possible
            else: #there is no wall and no box
                moves.append(Node(new_position, node.boxes, node, direction, node.depth + 1))


    def get_new_boxes(self, boxes, player, direction):
        new_boxes = set()

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

            new_boxes.add(b)



        return new_boxes
    """ Check is box can bu pushed, for each pusheable box if checkDeadlocks is true,
     check if the resulting box position will result in a deadlock"""
    def can_push_box(self, boxes, moved_player, direction, checkDeadlocks):
        
        if(direction == LEFT):
            pushed_box = (moved_player[0] -1, moved_player[1])
        elif(direction == RIGHT):
            pushed_box = (moved_player[0] + 1, moved_player[1])
        elif(direction == UP):
            pushed_box = (moved_player[0], moved_player[1] + 1)
        else:  
            pushed_box = (moved_player[0], moved_player[1] - 1)

        if(checkDeadlocks): # deadlock check turned on
            
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
            
        return pushed_box not in self.walls and pushed_box not in boxes # deadlock check turned off

    def is_completed(self, node):
        for box in node.boxes:
            if box not in self.goals:
                return False

        return True

    