#A Node has the player position and boxes positions

class Node:

    def __init__(self, player, boxes, prev, direction, depth, heuristic=0):
        self.prev = prev
        self.player = player
        self.boxes = boxes
        self.direction = direction
        self.depth = depth
        self.h = heuristic

    def __str__(self):
        return "player(%s) - boxes(%s) - direction(%s)"%(self.player, self.boxes,self.direction)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        f1 = self.depth + self.h
        f2 = other.depth + other.h

        if(f1 == f2):
            return self.h < other.h

        return f1 < f2

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and other.player == self.player and other.boxes == self.boxes)

    def __hash__(self):
        return hash((self.player,frozenset(self.boxes)))
