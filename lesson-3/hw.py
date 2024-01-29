class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.area = self.a * self.b

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        return self.area - other.area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __len__(self):
        return (self.a + self.b) * 2


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    @classmethod
    def get_count(cls):
        print(cls.__count)

    def __str__(self):
        return str(self.__dict__)


class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cinderella(self, cinderellas: list[Cinderella]):
        for cinderella in cinderellas:
            if cinderella.foot_size == self.shoe_size:
                print(cinderella)
                return
        print("Not Found")


cinder_list: list[Cinderella] = [
    Cinderella("Olha", 15, 30),
    Cinderella("Kamila", 21, 28),
    Cinderella("Kira", 32, 31),
    Cinderella("Karina", 18, 27),
]

prince = Prince("Mikey", 25, 28)
prince.find_cinderella(cinder_list)


from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Book name: {self.name}")


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Magazine name: {self.name}")


class Main:
    __printable_list: list[Printable] = []

    @classmethod
    def add(cls, item):
        if isinstance(item, (Magazine, Book)):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Book("book2"))
Main.add(Magazine("magazine2"))
Main.add(Book("book3"))
Main.add(Magazine("magazine1"))
Main.add(Book("book4"))
Main.add(Magazine("magazine3"))
Main.add(Book("book1"))
Main.add("dddddd")

Main.show_all_magazines()
Main.show_all_books()


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.area = self.a * self.b

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        return self.area - other.area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __len__(self):
        return (self.a + self.b) * 2


# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Cinderella(Human):
#     __count = 0

#     def __init__(self, name, age, foot_size):
#         super().__init__(name, age)
#         self.foot_size = foot_size
#         Cinderella.__count += 1

#     @classmethod
#     def get_count(cls):
#         print(cls.__count)

#     def __str__(self):
#         return str(self.__dict__)


# class Prince(Human):
#     def __init__(self, name, age, shoe_size):
#         super().__init__(name, age)
#         self.shoe_size = shoe_size

#     def find_cinderella(self, cinderellas: list[Cinderella]):
#         for cinderella in cinderellas:
#             if cinderella.foot_size == self.shoe_size:
#                 print(cinderella)
#                 return
#         print('Not Found')


# cinder_list: list[Cinderella] = [
#     Cinderella('Olha', 15, 30),
#     Cinderella('Kamila', 21, 28),
#     Cinderella('Kira', 32, 31),
#     Cinderella('Karina', 18, 27),
# ]

# prince = Prince('Mikey', 25, 28)
# prince.find_cinderella(cinder_list)


# class Printable(ABC):
#     @abstractmethod
#     def print(self):
#         pass


# class Book(Printable):
#     def __init__(self, name):
#         self.name = name

#     def print(self):
#         print(f'Book name: {self.name}')


# class Magazine(Printable):

#     def __init__(self, name):
#         self.name = name

#     def print(self):
#         print(f'Magazine name: {self.name}')


# class Main:
#     __printable_list: list[Printable] = []

#     @classmethod
#     def add(cls, item):
#         if isinstance(item, (Magazine, Book)):
#             cls.__printable_list.append(item)

#     @classmethod
#     def show_all_magazines(cls):
#         for item in cls.__printable_list:
#             if isinstance(item, Magazine):
#                 item.print()

#     @classmethod
#     def show_all_books(cls):
#         for item in cls.__printable_list:
#             if isinstance(item, Book):
#                 item.print()


# Main.add(Book('book2'))
# Main.add(Magazine('magazine2'))
# Main.add(Book('book3'))
# Main.add(Magazine('magazine1'))
# Main.add(Book('book4'))
# Main.add(Magazine('magazine3'))
# Main.add(Book('book1'))
# Main.add('dddddd')

# Main.show_all_magazines()
# Main.show_all_books()
