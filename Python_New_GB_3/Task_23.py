# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает
# количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально.

sp = [0, -1, 5, 2, 3, 1, -1]
count = 0

for i in range(1, len(sp)):
    if sp[i] > sp[i-1] and i > 0:
        count += 1

print(count)

list_1 = [1, 2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
k = 1
count = 0

for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1

print(count)


