# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод: 
# 1 2 3 2 3 
# Вывод:
# 2

from random import randint

def find_equal_count(input_list):
    sum = 0
    list_unique = set(input_list)
    for i in list_unique:
        sum += sp.count(i)//2
    return sum

list_lenth = int(input("введите число элементов: "))
print(sp := [randint(1, 10) for x in range(list_lenth)])

print(find_equal_count(sp))
