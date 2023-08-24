# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while
# Input: 5
# Output: 120```


num = int(input("Введите число: "))

fact = 1
index = 1
while index <= num:
    fact = fact * index
    index +=1

    print(int(fact))

# def input_num():
#     num = int(input("Input num: "))
#     return num
#
# def fact(num):
#     product = 1
#
#     i = 1
#     while i <= num:
#         product *= i
#         i += 1
#     print(product)
#
# n = input_num()
#
# fact(n)