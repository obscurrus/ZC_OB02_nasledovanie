class User:
    def __init__(self, id, name, access_level='user'):
        self.__id = id
        self.__name = name
        self.__access_level = access_level

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_access_level(self, access_level):
        self.__access_level = access_level
        print(f'Access level {self.__name} changed to {access_level}')

    def __str__(self):
        return f'ID: {self.__id}, Name: {self.__name}, Access Level: {self.__access_level}'

    def __repr__(self):
        return f'User({self.__id}, {self.__name}, {self.__access_level})'


class Admin(User):
    def __init__(self, id, name, access_level='admin'):
        super().__init__(id, name, access_level)
        self.__users_dict = {}

    def add_user(self, user):
        if isinstance(user, User):
            self.__users_dict[user.get_id()] = user
            print(f'User {user.get_id()} added')

    def remove_user(self, user_id):
        if user_id in self.__users_dict:
            del self.__users_dict[user_id]
            print(f'User {user_id} removed')

    def get_users(self):
        return list(self.__users_dict.values())

    def get_users_generator(self):
        for user in self.__users_dict.values():
            yield user

    def __str__(self):
        return f'Admin(ID: {self.get_id()}, Name: {self.get_name()}, Access Level: {self.get_access_level()})'

    def __repr__(self):
        return f'Admin({self.get_id()}, {self.get_name()}, {self.get_access_level()})'



''' testing zone '''

users = [
    User(1, 'Buba'),
    User(2, 'Zhlob'),
    User(3, 'Luntik'),
    User(4, 'Hren'),
    User(5, 'Sbugra'),
]

admin = Admin(0, 'Avatar_of_Uusikaupunki')

for user in users:
    admin.add_user(user)

print(admin)
print(list(admin.get_users_generator()))

admin.remove_user(3)
print(admin.get_users())


# Тестовая функция

def test_function(user):
    if user.get_access_level() == 'admin':
        print(f"{user.get_name()} has access level {user.get_access_level()} Function executed successfully.")
    else:
        print(f"{user.get_name()} has access level {user.get_access_level()}. Access denied.")


test_function(admin)
for user in admin.get_users_generator(): test_function(user)

