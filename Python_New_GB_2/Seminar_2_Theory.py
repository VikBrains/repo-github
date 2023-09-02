from random import randint
import time

def show_test(upper: int) -> str :
    n = 1
    #print(randint(1, upper))
    print(time.time() )
    return "n"

print(show_test(10))

sp = [55,111, True, "sssss", [55, 77, 88]]

# for i in range(len(sp)):   # печать поэлементно по индексу
#    print(sp[i], end = " ")

# print(end = "\n")          # печать поэлементно по очереди написания
# for el in sp:
#     print(el, end = " ")

# print(end = "\n")
# for item in enumerate(sp):   # печать парами счётчик + элемент (счётчик с "0")
#     print(item)
