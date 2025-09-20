from user import user as use
class usermanager:
    __users = []

    @classmethod
    def add_user(cls, User):
        if isinstance(User, use):
            cls.__users.append(User)
        else:
            print("Invalid user object.")

    @classmethod
    def find_user(cls,mail, password):
        for us in cls.__users:
            if us.email == mail and password == password:
                return us
        return None

    @classmethod
    def get_all_users(cls):
        return cls.__users
    

    #print(__users)
    


    