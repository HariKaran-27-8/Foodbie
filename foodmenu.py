from Abstractitem import Abstractitem
from fooditem import Fooditem

class Foodmenu(Abstractitem):
    def __init__(self,dish_name):
        super().__init__(dish_name)
        self.__Fooditems=[]

    @property
    def Fooditems(self):
        return self.__Fooditems
    
    @Fooditems.setter
    def Fooditems(self,Fooditems):
        for item in Fooditems:
            if not isinstance(item,Fooditem):
                print(f"Not a valid Fooditem: {item}")
                return
        self.__Fooditems=Fooditems

    def DisplayItem(self,start):
        print(f"{start} ->Menu: {self.dish_name} ")