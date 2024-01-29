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


# class User:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def del_name(self):
#         del self.__name


# user = User("Kris", 18)
# print(user.get_name())
# user.set_name("Lol")
# user.del_name()
# print(user.get_name())
# print(user.set_name("Lol"))


# class User:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age

#     def __get_name(self):
#         return self.__name

#     def __set_name(self, name):
#         self.__name = name

#     def __del_name(self):
#         del self.__name

#     name = property(fget=__get_name, fset=__set_name, fdel=__del_name)


# user = User("Kris", 18)
# user.name = "Test"
# print(user.name)


# class User:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age

#     @property
#     def name(self):
#         return self.__name

#     @name.fset
#     def name(self, name):
#         self.__name = name

#     @name.fdel
#     def name(self):
#         del self.__name


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return self.b + self.a

    def area(self):
        return self.b * self.a


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        return self.a * self.b * self.c


shapes: list[Shape] = [
    Triangle(1, 2, 3),
    Rectangle(
        2,
        3,
    ),
    Triangle(4, 5, 9),
]

for shape in shapes:
    print(shape.area())
    print(shape.perimeter())
