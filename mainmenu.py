from foodmanager import Foodmanager
from cart import Cart

class Mainmenu:

    __options = {
        1: 'View Restaurants',
        2: 'Search Food Items',
        3: 'Show Food Items',
        4: 'Search by Restaurant',
        5: 'Logout'
    }

    def __init__(self):
        self.__foodmanager = Foodmanager()

    def ViewRestaurants(self):
        for i,res in enumerate(self.__foodmanager.restaurants,1):
            res.DisplayItem(i)
        choice=int(input("please choose restaurant...")) 
        rest=self.__foodmanager.restaurants[choice-1]   
        self.ShowFoodMenus(rest.Foodmenus)

    
    def SearchFoodItems(self):
        search_term = input("Enter food item name to search: ")
        self.__foodmanager.search_food_items(search_term)

    def ShowFoodItems(self,Fooditems=None):
        if Fooditems is not None:
            for i,items in enumerate(Fooditems,1):
                items.DisplayItem(i)
            
            choice=list(map(int,input("please choose food items (comma separated for multiple): ").split(',')))
            cart=Cart(Fooditems,choice)
            cart.process_order(Fooditems)
        else:
            for item in self.__foodmanager.fooditems:
                print(f"***Dish: {item.dish_name} | Rating: {item.rating} | Price: {item.price} | Description: {item.description}")
                        

    def SearchbyRestaurant(self):
        restaurant_name = input("Enter restaurant name to search: ")
        rest=self.__foodmanager.findrestaurant(restaurant_name)
        self.ShowFoodMenus(rest.Foodmenus)
    
    def Logout(self):
        print("Logging out...")
        quit()

    def ShowFoodMenus(self,menus):
           print("\n\n list of menus available")
           for i,menu in enumerate(menus, start=1):
                menu.DisplayItem(i) 
           choice=int(input("please choose menu...")) 
           fooditems=menus[choice-1].Fooditems
           self.ShowFoodItems(fooditems)    


    def start(self):
        while True:
            for option in Mainmenu.__options:
                print(f"{option}. {Mainmenu.__options[option]}" , end=" | ")
            try:
                choice=int(input("\nPlease select an option: "))
                value=Mainmenu.__options[choice].replace(" ","")
                getattr(self, value)()
            except (ValueError, KeyError):
                print("Invalid option. Please try again.")
            