# Heuristics
# h1 = manhattan distance box-player
# h2 = min manhattan distance box-goal (Minimun lower bound)
# h3 = #obstacles to avoid
# h4 = 

# Strategy --> Mix:  h = Max(h1, h2, h3) AND deadlocks

class Heuristic:

    def __init__(self, board, heuristic):
        self.board = board
        self.heuristics = {
            'lower_bound': self.h_simple_lower_bound
        }
        self.h = self.heuristics[heuristic]
 
   

    def h_simple_lower_bound(self, node):
        #sum of the distances of each box to its nearest goal
        md = 0
        min = None
        for box in node.boxes: 
            for goal in self.board.goals:
                aux = self.manhattan_distance(box, goal)
                if(min is None or aux < min):
                    min = aux
            md += min
            min = None          
        return md

    def h_get_obstacles_to_avoid(node):
        pass
        

    def apply(node,board): 
        h1 = h_manhattan_distance_boxes_goals(node) #box-goal
        h2 = get_obstacles_to_avoid() 
        h3 = manhattan_distance() #player-goal
        
        print(h1)
        print(h2)
        print(h3)
        
        return h1 #voy probando con cada heuristica a ver cual es la mejor, hago un analisis y me quedo con una.

    def manhattan_distance(self, point1, point2): # |x1 - x2| + |y1 - y2|.
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    
    def sort_by_f(n1, n2):
        h1 = n1.h
        h2 = n2.h
        f1 = n1.depth + h1
        f2 = n2.depth + h2

        if(f1 < f2): return -1
        elif(f1 > f2): return 1
        else:
            if(h1 < h2): return -1
            elif(h1 > h2): return 1
            else: return 0

    def sort_by_h(n1, n2):
        h1 = n1.h
        h2 = n2.h

        if(h1 < h2): return -1
        elif(h1 > h2): return 1
        else: return 0


    def sort_nodes(self, nodes, sort_func):
        return sorted(nodes, key=sort_func)