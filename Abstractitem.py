from abc import ABC, abstractmethod

class Abstractitem(ABC):
    def __init__(self,dish_name,rating=None):
        self.dish_name = dish_name
        self.rating = rating

    @abstractmethod
    def DisplayItem(self,start):
        pass
