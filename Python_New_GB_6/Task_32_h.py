# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [ 1, 5, 88, 100, 2, -4]
# min = 33
# max = 200
# Ответ: [2, 3]
# Вывод: [1, 9, 13, 14, 19]

# import random
# n = int(input("введите размер массива: "))
# list_input = [random.randint(-100, 250) for _ in range(n)]
# print(list_input)

# min = int(input("введите минимальное значение: "))
# max = int(input("введите максимальное значение: "))

list_input = [ 1, 5, 88, 100, 2, -4]
max = 200
min = 33

list_output = []

for i in range(len(list_input)):
    if min <= list_input[i] <= max:
        list_output.append(i)
print(list_output)
