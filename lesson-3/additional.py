class User:
    count = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Kirill", 26)


print(user.name)
