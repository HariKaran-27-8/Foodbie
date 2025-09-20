import re,user,usermanager
from mainmenu import Mainmenu

class login_system:

    def Login(self):
        mail=input("Enter your email: ")
        password=input("Enter your password: ")

        User=usermanager.usermanager.find_user(mail,password)

        if User is not None:
            print(f"Welcome back, {User.name}!")
            menu=Mainmenu()
            menu.start()
        else:
            print("Invalid email or password. Please try again.")


    def Register(self):
        name=input("Enter your name: ")
        if not re.match(r"^[A-Za-z ]+$", name):
            print("Invalid name (only letters and spaces allowed).")
        email=input("Enter your email: ") 
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            print("Invalid email format.")  
        password=input("Enter your password: ")
        if not re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{6,}$", password):
            print("Invalid password (must be 6+ chars with upper, lower, number).")
        phone=input("Enter your phone number: ")
        if not re.match(r"^[6-9]\d{9}$", phone):
            print("Invalid phone (must be 10 digits starting with 6-9).")

        User=user.user(name,email,password,phone)

        usermanager.usermanager.add_user(User)
        print("Registration successful!")

    def Guest(self):
        return usermanager.usermanager.get_all_users()

    def Exit(self):
        print("Thank you for visiting Foodbie's ocean of tastes. Goodbye!")
        quit()
    
    def validate_choice(self,choice):
       
        getattr(self, choice)()
     

class Foodapp:

    login_options = {1: 'Login', 2: 'Register', 3: 'Guest',4: 'Exit'}

    @staticmethod
    def home():
        print( "Welcome to the Foodbie's ocean of tastes!")

        # menu=Mainmenu()
        # menu.start()

        global login_system
        login_system=login_system()
        print("Please select an option:")
        while True:
            for key, value in Foodapp.login_options.items():
                print(f"{key}. {value}")
            try:
                key = input(" Please select an option:  ")
                login_system.validate_choice(Foodapp.login_options[int(key)])
            except (ValueError, KeyError):
                print("Invalid option. Please try again.")
        