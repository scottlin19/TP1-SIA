from abc import ABC, abstractmethod
class SearchMethod(ABC):
    
    def __init__(self):
        self.nodes_expanded = 0
        self.visited = set()
        self.queue = []
        super().__init__()

    @abstractmethod
    def search(self,board):
        pass