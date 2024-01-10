# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

string = "as 23 fdfdg544"


def get_int(str):
    print(", ".join(ch for ch in str if ch.isdigit()))


get_int(string)
