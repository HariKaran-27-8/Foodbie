from fooditem import Fooditem
from foodmenu import Foodmenu
from Restaurant import Restaurant


class Foodmanager:
    def __init__(self):
        self.restaurants=self.__prepare_restaurants()
        
    
    def __prepare_fooditems(self):
        fooditem1=Fooditem("Pizza",4.5,8.99,"Delicious cheese pizza with fresh toppings")
        fooditem2=Fooditem("mutton biryani",4.7,10.99,"Aromatic basmati rice with tender mutton pieces")
        fooditem3=Fooditem("Pasta",4.0,7.99,"Creamy Alfredo pasta with chicken")
        fooditem4=Fooditem("paneer tikka",4.3,9.99,"Spicy grilled paneer cubes with bell peppers")
        fooditem5=Fooditem("ramen noodles",4.6,11.99,"Savory broth with noodles, pork, and soft-boiled egg")
        fooditem6=Fooditem("Caesar Salad",4.2,6.99,"Crisp romaine lettuce with Caesar dressing and croutons")
        return [fooditem1,fooditem2,fooditem3,fooditem4,fooditem5,fooditem6]
        
    def __prepare_foodmenus(self):

        fooditems=self.__prepare_fooditems()

        menu1=Foodmenu("Continental")
        menu1.Fooditems=[fooditems[0],fooditems[2],fooditems[5]]
        menu2=Foodmenu("indian")
        menu2.Fooditems=[fooditems[1],fooditems[3]]
        menu3=Foodmenu("Chinese")
        menu3.Fooditems=[fooditems[4]]
        menu4=Foodmenu("Diet")
        menu4.Fooditems=[fooditems[5]]
        return [menu1,menu2,menu3,menu4]

    def __prepare_restaurants(self):

        foodmenus=self.__prepare_foodmenus()

        restaurant1=Restaurant("Foodie's Delight",4.5,"Downtown","10% off on all orders")
        restaurant1.Foodmenus=[foodmenus[0],foodmenus[1]]
        restaurant2=Restaurant("Taste Buds",4.2,"Uptown","Free dessert with every meal")
        restaurant2.Foodmenus=[foodmenus[2],foodmenus[3]]
        restaurant3=Restaurant("Gourmet Haven",4.8,"Midtown","20% off on weekends")
        restaurant3.Foodmenus=[foodmenus[0],foodmenus[2]]
        restaurant4=Restaurant("Culinary Corner",4.0,"Suburbs","Buy one get one free on select items")
        restaurant4.Foodmenus=[foodmenus[3]]
        return [restaurant1,restaurant2,restaurant3,restaurant4]
    def findrestaurant(self,restaurant_name):
        found=False
        for res in self.restaurants:
            if restaurant_name.lower() in res.dish_name.lower():
                found=True
                return res
        if not found:
            print("No restaurants found with that name.")

    def search_food_items(self,search_term):
        found_items=[]
        for res in self.restaurants:
            for menu in res.Foodmenus:
                for item in menu.Fooditems:
                    if search_term.lower() in item.dish_name.lower():
                        found_items.append(item)
        if found_items:
            print(f"Found {len(found_items)} items matching '{search_term}':")
            for i,item in enumerate(found_items,1):
                item.DisplayItem(i)
            choice = input("Type 'add' to add an item to cart or 'back' to return: ").strip().lower()
            if choice == 'add':
                item_num = input("Enter the item number to add to cart: ").strip()
                try:
                    item_index = int(item_num) - 1
                    # Use enumerate to display items again for clarity
                    print("Available items:")
                    for idx, item in enumerate(found_items, 1):
                        print(f"{idx}. {item.dish_name}")
                    print("1. Add an item to cart")
                    print("2. Go back")
                    action = input("Enter your choice (1 or 2): ").strip()
                    if action == '1':
                        item_num = input("Enter the item number to add to cart: ").strip()
                        try:
                            item_index = int(item_num) - 1
                            if 0 <= item_index < len(found_items):
                                selected_item = found_items[item_index]
                                if not hasattr(self, 'cart'):
                                    self.cart = []
                                self.cart.append(selected_item)
                                print(f"{selected_item.dish_name} added to cart.")
                            else:
                                print("Invalid item number.")
                        except ValueError:
                            print("Please enter a valid number.")
                    elif action == '2':
                        print("Returning to previous menu.")
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Please enter a valid number.")
            
        else:
            print(f"No items found matching '{search_term}'.")