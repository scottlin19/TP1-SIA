from abc import ABC, abstractmethod
class SearchMethod(ABC):
    
    def __init__(self):
        super().__init__()

    @abstractmethod
    def search(self,board):
        pass