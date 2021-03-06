#A Node has the player position and boxes positions

class Node:

    def __init__(self, player, boxes):
        self.player = player
        self.boxes = boxes

    def __str__(self):
        return "[%s,%s]"%(self.player, self.boxes) 