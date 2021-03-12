from abc import ABC, abstractmethod
class SearchMethod(ABC):
    
    def __init__(self,checkDeadlocks):
        super().__init__()
        self.checkDeadlocks = checkDeadlocks

    @abstractmethod
    def search(self,board):
        pass