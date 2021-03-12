from node import Node
from sokoban_render import render
from algorithms.searchMethod import SearchMethod
from searchResults import SearchResults
from metrics import Metrics
 
LIMIT_INCREASE = 10

class IDA_STAR(SearchMethod):
    def __init__(self, limit,checkDeadlocks):
        super().__init__(checkDeadlocks)
        self.limit = limit
        self.visited = set()
        self.metrics = Metrics('IDDFS',False,0,0,0,0, 0, [])
        self.queue = []
        self.solution_found = False
    
    def search(self,board):
        
        node = Node(board.player, board.boxes, None, None, 0)