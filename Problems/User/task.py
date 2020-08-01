class User:
    # create the class attributes
    n_active = 0
    users = []

    # create the __init__ method
    def __init__(self, active, user_name):
        self.user_name = user_name
        self.active = active
        if active:
            User.n_active += 1
        self.users.append(user_name)


# user = User(True, "Rapho")
# user2 = User(True, "Mike")
# print(user.active)
# print(user.user_name)
# print(User.users)
# print(User.n_active)
