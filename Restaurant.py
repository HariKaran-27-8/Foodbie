from Abstractitem import Abstractitem
from foodmenu import Foodmenu

class Restaurant(Abstractitem):
    def __init__(self,dish_name,rating,location,offers):
        super().__init__(dish_name,rating)
        self.location=location
        self.offers=offers
        self.Foodmenu=None
    
    @property
    def Foodmenus(self):
        return self.__Foodmenus
    
    @Foodmenus.setter
    def Foodmenus(self,Foodmenus):
        for item in Foodmenus:
            if not isinstance(item,Foodmenu):
                print(f"Not a valid Foodmenu: {item}")
                return
        self.__Foodmenus=Foodmenus

    def DisplayItem(self,start):
        print(f"{start} =>  {self.dish_name} | Rating: {self.rating} ")