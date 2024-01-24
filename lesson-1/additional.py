# f = 5.99999
# i = int(f)
# print(i)

# p = 5
# t = float(p)
# print(t)

# e = 5
# r = str(e)
# print(type(r))

# only 0 it's False

# i = 30 // 5
# print(type(i))

# t = 11 % 3
# print(t)

# print(5 != 6)

# i = 2
# i += 5
# i %= 2
# print(i)

# i = 7

# if i == 6 or i == 5:
#     print("it's 6 or 5")
# elif i == 7 and True:
#     print("it's 7")
# elif i == 8:
#     print("it's 8")
# else:
#     print("error")

# i = -5
# while i <= 5:
#     print(i)
#     i += 1
# else:
#     print("ok")

# for i in range(10, 100, 5):
#     print(i)

# for i in range(50):
#     if i == 5 or i == 6:
#         # break
#         continue
#     print(i)
# else:
#     print("the end")
# print("some code")

# str = "hello, world!"

# print(str[0])

# for i in str:
#     print(i)

# print(str[0:5:2])

# str = "1234 !"
# print(len(str))
# print(str.index("3"))
# print(str.rindex("3"))
# print(str.find("3"))
# print(str.rfind("3"))

# str = "/gmail.com"
# print(str.isspace())
# print(str.isalpha())
# print(str.endswith("com"))
# print(str.startswith("g"))
# print(str.lower())  # and the same with upper and capitalize
# print(str.islower())
# print(str.replace(".com", ".ua", 1))
# print(str.split("."))
# print(str.strip("/"))


# str0 = "hello "
# str1 = "world"
# print(str0 + str1 * 2)
# str = r"hello \tworld"
# print(str)

# l = [1, 2, 5.2, "dtg", True]

# l1 = [6, 7]

# print(l + l1)

# t = [1, 2, 3, 4, 5]
# l = (1, 2, 3, 4, 5)

# print(t.__sizeof__(), l.__sizeof__())

# d = {"name": "Bob", "age": 25, 11: 123}
# print(d.popitem())
# print(d.setdefault("age"))
# print(d.setdefault("lol"))
# print(d)


# set = {1, 1, 1, 1, 2, 3, 4, 4, 4, 4}  # random order

# for i in set:
#     print(i)

# set.add(10)
# set.remove(1)
# set.discard(1)  # without error if doesn't exist

# print(set)

# set1 = {1, 2, 3, 4, 5}
# set2 = {9, 2, 10, 4, 5}

# print(set1.symmetric_difference(set2))
# print(set1.union(set2))
# print(set1.issubset(set2))
# print(set1.isdisjoint(set2))

###################################### FUNCTIONS ######################################


# num1 = 6
# num2 = 3.3


# def sum():
#     sum = num1 + num2
#     print(sum)


# def sum(n1=1, n2=2):
#     return n1 + n2


# x = sum(n2=10)
# print(x)


# def some(*args, **kwarks):
#     return args, kwarks


# print(some(1, 2, 3, 4, 5, age=2))

# l = [1, 2, 3, 4]

# a, b, c, _ = l
# a, *_, b = l
# *_, b = l


# print(b)

# l = [1, 2, 3, 4]

# l2 = [*l]
# print(l is l2)
# print(l == l2)
