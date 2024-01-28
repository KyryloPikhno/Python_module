# class User:
#     count = 1

#     __slots__ = ("name", "age")

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# user = User("Kirill", 26)
# print(user.name)


# class User:
#     def __init__(self, name):
#         self.__name = name  # ptivate

#     def ger_name(self):
#         print(self.__name)


# user = User("Lol")

# user.ger_name()


# class Car:
#     def __init__(self, brand):
#         self.brand = brand


# class Tools:
#     def greeting(self):
#         print("hello")


# class SuperCar(Car, Tools):
#     def __init__(self, brand, model):
#         super().__init__(brand)

#         self.model = model


# car = SuperCar("Audi", "V8")
# car.greeting()


class User:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def del_name(self):
        del self.__name


user = User("Kris", 18)
# print(user.get_name())
# user.set_name("Lol")
# user.del_name()
# print(user.get_name())
# print(user.set_name("Lol"))
