from node import Node
from sokoban_render import render
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults
from metrics import Metrics
from algorithms.informed.heuristic import Heuristic
import math
import bisect

class IDA_STAR(SearchMethod):
    def __init__(self, heuristic, checkDeadlocks):
        super().__init__(checkDeadlocks)
        self.heuristic = heuristic
        self.visited = set()
        self.metrics = Metrics('IDA*',False,0,0,0,0, 0, [])
        self.queue = []
    
    def search(self,board):

        self.heuristic = Heuristic(board, self.heuristic)
        
        node = Node(board.player, board.boxes, None, None, 0)
        node.h = self.heuristic.h(node)
        bound = node.h

        while True:
            self.visited = set()
            self.queue = [node]
            min_f = math.inf

            while self.queue:
                curr = self.queue.pop(0)
                self.visited.add(curr)

                if(board.is_completed(curr)):
                    self.metrics.success = True
                    self.metrics.frontier = len(self.queue)
                    return SearchResults(self.metrics, curr)

                moves = board.get_possible_moves(curr, self.checkDeadlocks)
                if moves:
                    self.metrics.nodes_expanded += 1

                for move in moves:
                    if move in self.visited:
                        continue

                    move.h = self.heuristic.h(move)
                    move_f = move.depth + move.h

                    if(move_f > bound):
                        if(move_f < min_f):
                            min_f = move_f
                        continue
                    
                    bisect.insort(self.queue, move)

            bound = min_f
                    



            