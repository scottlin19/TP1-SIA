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
            'lower_bound': self.h_simple_lower_bound, #por ahora la mejor. Es consistente --> admisible
            'player_boxes': self.h_sum_distances_player_boxes, #no es consistente pero encontro la optima. No puedo asegurar que sea no admisible
            'free_goals': self.h_get_free_goals, #es < que lower_bound y tarda mas --> No conviene agarrar esta. Es consistente --> es admisible pero creo que es trivial
            'player_box_goal': self.h_player_box_goal #no es consistente, no encontro la optima --> no admisible y encima tardó más
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

    """def h_get_obstacles_to_avoid(self, node):
        #cajas/paredes que tengo que esquivar para llegar a goal --> Goal-caja-jugador tienen que estar en idem fila o en idem columna
        avoid = 0
        player = node.player
        boxes = node.boxes
        goals = self.board.goals
        obstacles = []
        obstacles.append(boxes).append(self.board.walls)
        
        for goal in goals:
            for obstacle in obstacles: 
                list_x = list(player[0], obstacle[0], goal[0]) 
                list_y = list(player[1], obstacle[1], goal[1]) 
                if (list_x in row or list_y in col):
                    avoid +=1 
        
        return avoid"""
    
    def h_get_free_goals(self, node):
        #Goals that do not have a box yet. I think it is trivial 
        boxes = node.boxes
        goals = self.board.goals
        occupied = 0
        for box in boxes:
            for goal in goals: 
                if(box[0] == goal[0] and box[1] == goal[1]):
                    occupied +=1
        
        return len(goals) - occupied
  
    def h_sum_distances_player_boxes(self, node):
        #Sum of the distances between player and each box 
        boxes = node.boxes 
        player = node.player
        md = 0
        for box in boxes: 
            md += self.manhattan_distance(player, box)
        return md

    def h_player_box_goal(self, node):
        boxes = node.boxes 
        player = node.player
        goals = self.board.goals
        md = 0
        min = None
        for box in boxes: 
            md += self.manhattan_distance(player, box)
            for goal in goals:
                aux = self.manhattan_distance(box, goal)
                if(min is None or aux < min):
                    min = aux
            md += min
        
        return md
        
        
    def manhattan_distance(self, point1, point2): # |x1 - x2| + |y1 - y2|.
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    
    def sort_by_f(self, item):
        h = item.h
        f = item.depth + h
        return (f,h)
 
    def sort_by_h(self, item):
        return item.h

    def sort_nodes(self, nodes, sort_func):
        return sorted(nodes, key=sort_func)