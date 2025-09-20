
class Cart:

    paymentoptions = {
        1: 'Credit Card',
        2: 'Debit Card',
        3: 'UPI',
        4: 'cash on delivery'}

    def __init__(self,items,choices):
        #self.items=[]
        self.choices=choices
        self.fooditems=self.__AddToCart(items)
        

    def __AddToCart(self,item):
        fooddict={}
        for choice in self.choices:

            if choice > len(item):
                raise KeyError(f"Invalid choice: {choice}")

            if choice in fooddict:
                fooddict[choice]+=1
            else:
                fooddict[choice]=1
        return fooddict
    
    def process_order(self,fooditems):
        total=0
        for item in self.fooditems:
            price=fooditems[item-1].price * self.fooditems[item]
            total+=price
            print(f" {fooditems[item-1].dish_name} x {self.fooditems[item]} = {price}")
        print(f"Total Amount: {total}")
        choice = int(input("\nEnter 1 to View Cart, 2 to Proceed with Transaction: "))
        if choice == 1:
            self.ViewCart(self.fooditems)
        elif choice == 2:
            self.payment(total)
        else:
            print("Invalid option selected.")
        

    def payment(self,total):
        payment_methods = {
            1: 'Credit Card',
            2: 'Debit Card',
            3: 'UPI',
            4: 'Net Banking',
            5: 'Cash on Delivery'
        }

        print(f"\n🛒 Your total bill is: ₹{total:.2f}")
        print("\nAvailable Payment Methods:")
        for key, value in payment_methods.items():
            print(f"{key}. {value}")

        try:
            selected = int(input("Choose your payment method: "))
            if selected not in payment_methods:
                print("❌ Invalid payment method selected. Transaction failed.")
                return None

            payment_info = {"method": payment_methods[selected], "status": "Failed", "amount": total, "details": ""}

            # Validation for each payment method
            if selected == 1:  # Credit Card
                card = input("Enter Credit Card number: ")
                if not (card.isdigit() and len(card) == 16):
                    print("❌ Invalid Credit Card number. Transaction failed.")
                    return None
                payment_info["status"] = "Success"
                payment_info["details"] = f"**** **** **** {card[-4:]}"

            elif selected == 2:  # Debit Card
                card = input("Enter Debit Card number: ")
                if not (card.isdigit() and len(card) == 16):
                    print("❌ Invalid Debit Card number. Transaction failed.")
                    return None
                payment_info["status"] = "Success"
                payment_info["details"] = f"**** **** **** {card[-4:]}"

            elif selected == 3:  # UPI
                upi = input("Enter UPI ID: ")
                if "@" not in upi or len(upi) < 5:
                    print("❌ Invalid UPI ID. Transaction failed.")
                    return None
                payment_info["status"] = "Success"
                payment_info["details"] = upi

            elif selected == 4:  # Net Banking
                userid = input("Enter Net Banking User ID: ")
                password = input("Enter Net Banking Password: ")
                if len(userid) < 4 or len(password) < 4:
                    print("❌ Invalid Net Banking credentials. Transaction failed.")
                    return None
                payment_info["status"] = "Success"
                payment_info["details"] = f"NetBanking User: {userid}"

            elif selected == 5:  # Cash on Delivery
                contact = input("Enter your contact number: ")
                if not contact.isdigit() or len(contact) < 10:
                    print("❌ Invalid contact number. Transaction failed.")
                    return None
                payment_info["status"] = "Success"
                payment_info["details"] = f"Contact: {contact}"

            print(f"\n✅ Transaction successful! Paid ₹{total:.2f} using {payment_info['method']}")
            return payment_info

        except Exception as e:
            print(f"⚠️ Error: {e}. Transaction failed.")
            return None




    def RemoveItem(self,item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed item: {item}")
        else:
            print(f"Item not in cart: {item}")

    def ViewCart(self,fooditems):
        if not self.fooditems:
            print("Cart is empty")
            return
        print("Items in Cart:")
        for choice, qty in self.fooditems.items():
            food_item = fooditems[choice - 1]
            print(f"{choice}. {food_item.dish_name} | Price: {food_item.price} | Qty: {qty}")
        
           
        choice = int(input("\nEnter 1 to Proceed with Transaction, 2 to remove an item : "))
        if choice == 1:
            self.payment()
        elif choice == 2:
            item_no= int(input("Enter item number to remove: "))
            if 0 < item_no <= len(self.fooditems):
                self.RemoveItem(self.fooditems[item_no-1])
                self.ViewCart()
            else:
                print("Item not found in cart.")
        else:
            print("Invalid option selected.")