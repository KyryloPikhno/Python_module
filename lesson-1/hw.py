# strings

# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# string = "as 23 fdfdg544"


# def get_int(str):
# print(", ".join(ch for ch in str if ch.isdigit()))


# get_int(string)


# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі


# def get_letters(str):
#     print(", ".join(" ".join(ch if ch.isdigit() else " " for ch in str).split()))


# get_letters(string)


# list comprehension

# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = "Hello, world"

# print([ch for ch in greeting.upper()])


# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]


# print([i**2 for i in range(50) if i % 2])


# function

# - створити функцію яка виводить ліст


# def show_list(l):
#     for i in l:
#         print(i)


# show_list([1, 2, 3, 4])


# - створити функцію яка приймає три числа та виводить та повертає найбільше.


# def max_num(a, b, c):
#     res = max(a, b, c)
#     print(res)
#     return res


# max_num(10, 2, 22)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше


# def find_min_max(*args):
#     print(max(args))
#     return min(*args)


# - створити функцію яка повертає найбільше число з ліста


# def find_max_from_list(l):
#     return max(l)


# - створити функцію яка повертає найменьше число з ліста


# def find_min_from_list(l):
#     return min(l)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.


# def sum_of_list(l):
#     return sum(l)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.


# def avg_of_list(l):
#     return sum(l) / len(l)


# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'

# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


# def find_min_from_list():
#     return min(list)


# def remove_dublicates():
#     new_list = list.copy()
#     return list(set(new_list))


# def to_x():
#     new_list = list.copy()
#     print(["x" if not (i + 1) % 4 else item for i, item in enumerate(new_list)])


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції


# def square(n):
#     for i in range(n):
#         if i == 0 or i == n - 1:
#             print("*" * n)
#         else:
#             print("*" + " " * (n - 2) + "*")


# square(20)

# 3) вывести табличку множення за допомогою цикла while


# def multi_table():
#     size = 9
#     i = 1
#     while i <= size:
#         j = 1
#         while j <= size:
#             res = i * j
#             print("  " if res // 10 else "   ", end="")
#             print(res, end="")
#             j += 1
#         i += 1
#         print()


# multi_table()
