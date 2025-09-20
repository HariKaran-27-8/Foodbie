
# Foodbie: Online Food Order System
Foodbie is a console-based online food ordering system built using Python's Object-Oriented Programming (OOP) principles. It allows users to browse restaurants, view menus, search for food items, add them to a cart, and proceed with a simulated payment process.

## Features
*  **User Authentication:**
   *  **Login:** Existing users can log in with their email and password.
   *  **Register:** New users can create an account with name, email, password, and phone number validation.
   *  **Guest Mode:** Users can explore the system without logging in.
*  **Restaurant and Menu Management:**
   *  **View Restaurants:** Browse a list of available restaurants.
   *  **View Menus:** See the food menus offered by each restaurant.
*  **Food Item Management:**
   *  **Search Food Items:** Find specific food items across all restaurants.
   *  **Display Food Items:** View details of food items including dish name, rating, price, and description.
*  **Shopping Cart Functionality:**
   *  **Add to Cart:** Select multiple food items to add to your cart.
   *  **View Cart:** Review items currently in your cart.
   *  **Remove from Cart:** Remove unwanted items from the cart.
*  **Order Processing and Payment:**
   *  **Process Order:** Calculate the total amount for items in the cart.
   *  **Payment Gateway Simulation:** Choose from various payment methods (Credit Card, Debit Card, UPI, Net Banking, Cash on Delivery) with basic validation.
   *  **Order Saving:** Successful orders are saved to a `orders.json file`.
  
*  **Modular Design:** The system is structured using OOP, with clear separation of concerns into classes like `User`, `UserManager`, `AbstractItem`, `Fooditem`, `Foodmenu`, `Restaurant`, `Foodmanager`, `Cart`, `Mainmenu`, and `OrderSystem`.

## Getting Started
### Prerequisites
*  Python 3.x installed on your system.

### Installation
**Clone the repository:**
```bash
git clone <repository_url>
cd Foodbie-Online-Food-Order-System
```
(Replace `<repository_url>` with the actual URL of your repository if it's hosted on GitHub, GitLab, etc.)

**Navigate to the project directory:**
```bash
cd MultipleFiles
```
### Running the Application
To start the Foodbie application, run the `main.py` file:

```bash
python main.py
```

## How to Use
Upon running the application, you will be presented with a welcome message and login options:
```
Welcome to the Foodbie's ocean of tastes!
Please select an option:
1. Login | 2. Register | 3. Guest | 4. Exit |
 Please select an option:
```
### 1. Register
*  Choose option `2` to register a new account.
*  Follow the prompts to enter your name, email, password, and phone number. The system includes basic validation for these inputs.
### 2. Login
*  If you have an existing account, choose option `1` and enter your registered email and password.
*  Upon successful login, you will be directed to the main menu.
### 3. Guest Mode
*  Choose option `3` to explore the application as a guest. You can browse restaurants and food items, but you won't be able to save orders under a user profile.

### Main Menu Options (after Login or Guest)
Once in the main menu, you can perform various actions:

*  **1. View Restaurants:**
   *  Displays a list of available restaurants.
   *  You can then select a restaurant to view its food menus.
*  **2. Search Food Items:**
   *  Allows you to search for specific food items by name across all restaurants.
   *  If items are found, you can choose to add them to your cart.
*  **3. Show Food Items:**
   *This option is typically used after selecting a menu from a restaurant to display the items within that menu.
   *You can select multiple food items to add to your cart.
*  **4. Search by Restaurant:**
   *  Search for a restaurant by its name.
   *  If found, it will display the menus for that restaurant.
*  **5. Logout:**
   *  Exits the application.
### Cart and Payment Process
*  After adding items to your cart (either through "Search Food Items" or "Show Food Items"), you will be prompted to proceed with the transaction.
*  You can view your cart, which shows the selected items and their quantities.
*  When proceeding to payment, the total bill will be displayed, and you can choose from various payment methods.
*  Each payment method has basic input validation.
*  Upon successful payment, the order details will be saved to `orders.json`.

## Project Structure
```
MultipleFiles/
├── Abstractitem.py         # Abstract base class for items (Fooditem, Foodmenu, Restaurant)
├── cart.py                 # Handles shopping cart logic, adding/removing items, and payment processing
├── food.py                 # Contains login_system and Foodapp classes for user authentication and application entry
├── fooditem.py             # Represents a single food item
├── foodmanager.py          # Manages restaurants, food menus, and food items; handles search functionality
├── foodmenu.py             # Represents a food menu containing multiple food items
├── latertry.py             # (Potentially an older or experimental payment/order saving module)
├── main.py                 # Main entry point of the application
├── mainmenu.py             # Manages the main application menu and user interactions
├── orders.json             # Stores successful order details in JSON format
├── Restaurant.py           # Represents a restaurant with its details and menus
├── user.py                 # Defines the User class
└── usermanager.py          # Manages user accounts (add, find, get all users)
```

## Future Enhancements

*  **Persistent Data:** Implement database integration (e.g., SQLite) for storing user, restaurant, and order data more robustly.
*  **Order History:** Allow users to view their past orders.
*  **Admin Panel:** Create an admin interface for managing restaurants, menus, and users.
*  **Rating System:** Allow users to rate food items and restaurants.
*  **More Robust Input Validation:** Enhance validation for all user inputs.
*  **Error Handling:** Implement more comprehensive error handling.
*  **User Interface:** Consider a GUI framework (e.g., Tkinter, PyQt) for a more user-friendly experience.

## Contributing
    Feel free to fork the repository, make improvements, and submit pull requests.

## License
    This project is open-source and available under the [MIT License].
