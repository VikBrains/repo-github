# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод: 3 3 2 12
# (каждое число вводится с новой строки)

import random

n = int(input("введите размер массива 1: "))
array_1 = [random.randint(0, 15) for _ in range(n)]

m = int(input("введите размер массива 2: "))
array_2 = [random.randint(0, 15) for _ in range(m)]

print(array_1)
print(array_2)

array_res = [x for x in array_1 if x not in array_2]
print(array_res)
