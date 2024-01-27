# l = [1, 2]

# a, b = l

# tuple_1 = (1, 2)

# a = 5
# b = 7

# res = a, b

# b, a = (a, b)


# def decor(func):
#     def inner(*args, **kwargs):
#         print("*" * 20)
#         func(*args, **kwargs)
#         print("*" * 20)

#     return inner


# @decor
# @decor
# @decor
# def greeting(name):
#     print(f"hello, {name}")


# greeting("Lol")

# inner = decor(greeting)

# inner()

# for i in range(5):
#     pass


# def counter():
#     count = 0

#     def inc():
#         nonlocal count
#         count += 1
#         return count

#     return inc


# counter1 = counter()
# counter2 = counter()

# print(counter1())
# print(counter1())
# print(counter1())
# print(counter2())
# print(counter2())
# print(counter2())
# print(counter2())

# l = [1, 2, 3, -1, 2, 3, 4]

# l.sort()

# print(l)
