# def gen(name):
#     for ch in name:
#         yield ch


# g = gen("Kirill")
# print(next(g))
# print("something")
# print(next(g))


# def gen(name):
#     for ch in name:
#         yield ch
#         print("lol")


# g = gen("Kirill")

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# l = [i for i in range(50000000)]
# input()

# g = (i for i in range(3))
# print(next(g))
# print(next(g))
# print(next(g))

# for i in g:
#     print(i)

# try:
#     fffffff
#     print(6 / 0)
#     int("fffffff")
# except NameError as err:
#     print(f"Error: {err}")
# except ZeroDivisionError as err:
#     print(f"Error: {err}")
# except Exception as err:
#     print(f"Error: {err}")
# else:
#     print("Success")
# finally:
#     print("Finally")


# print("It works")

# from uuid import uuid1


# def gen_file_nmae():
#     while True:
#         yield f"{uuid1()}.png"


# g = gen_file_nmae()

# print(next(g))


# class MyRange:
#     def __init__(self, lenght):
#         self.__lenght = lenght
#         self.__counter = 0

#     # def __iter__(self):
#     #     return self

#     def __next__(self):
#         if self.__counter < self.__lenght:
#             res = self.__counter
#             self.__counter += 1
#             return res
#         raise StopIteration


# g = MyRange(5)

# print(next(g))


# def my_range(lenght):
#     count = 0
#     while count < lenght:
#         yield count
#         count += 1


# for i in my_range(5):
#     print(i)


# file = open("lesson-4/file.txt")
# res = file.read(1)
# print(res)


# try:
#     file = open("lesson-4/file.txt")
#     try:
#         print(file.read())
#     finally:
#         file.close()
# except Exception as err:
#     print(err)

# try:
#     with open("lesson-4/file.txt") as file:
#         print(file.read())
# except Exception as err:
#     print(err)


# try:
#     with open("lesson-4/file.txt", "w") as file:
#         file.write("something")
# except Exception as err:
#     print(err)
