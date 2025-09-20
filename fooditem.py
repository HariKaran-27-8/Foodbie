from Abstractitem import Abstractitem

class Fooditem(Abstractitem):
    def __init__(self,dish_name,rating,price,description):
        super().__init__(dish_name,rating)
        self.price=price
        self.description=description

    def DisplayItem(self,start):
        print(f"{start} -> Dish: {self.dish_name} | Rating: {self.rating} | Price: {self.price} | Description: {self.description}")
        