# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.

# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

set_1 = []
nums_1 = int(input("Введите число элементов множества 1: "))
for i in range(nums_1):
    num = int(input("Введите элемент множества: "))
    set_1.append(num)
print(set_1)

set_2 = []
nums_2 = int(input("Введите число элементов множества 2: "))
for i in range(nums_2):
    num = int(input("Введите элемент множества: "))
    set_2.append(num)
print(set_2)

sort_set = []
for i in (set_1 + set_2):
    if (set_1 + set_2).count(i) > 1 and i not in sort_set:
        sort_set.append(i)

print(sort_set)


# sort_set = sorted(set_1 & set_2)
# print(sort_set)
#

# from random import randint
#
# nums_1 = int(input('Введите кол-во элементов первого множества: '))
# set_1 = set(randint(-10, 10) for i in range(nums_1))
# print(set_1)
#
# nums_2 = int(input('Введите кол-во элементов второго множества: '))
# set_2 = set(randint(-10, 10) for i in range(nums_2))
# print(set_2)

# sort_set = sorted(set_1.intersection(set_2))
# print(sort_set)
