#A Node has the player position and boxes positions

class Node:

    def __init__(self, player, boxes, steps):
        self.player = player
        self.boxes = boxes
        self.steps = steps

    def __str__(self):
        return "player(%s) - boxes(%s)"%(self.player, self.boxes)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and other.player == self.player and other.boxes == self.boxes)

    def __hash__(self):
        return hash(self.__str__())