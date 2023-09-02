# Хакер Василий получил доступ к классному журналу и хочет заменить все свои
# минимальные оценки на максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


def maxV(arg):
    temp = 0
    for el in arg:
        if el > temp:
            temp = el
    return temp

def minV(arg):
    temp = arg[0]
    for el in arg:
        if el < temp:
            temp = el
    return temp

list1 = [1, 3, 3, 3, 4]

for i in range(len(list1)):
    if list1[1] == maxV(list1):
        list[i] == minV(list1)
print(list1)


# def change_value(mini, maxi, n):
#     if n < 0:
#         return
#     else:
#         if list1[n] == maxi:
#             list1[n] = mini
#         change_value(min, max, n - 1)

# list1 = [1, 3, 3, 3, 4]
# change_value(min(list1), max(list1), len(list1) - 1)
# print(list1)