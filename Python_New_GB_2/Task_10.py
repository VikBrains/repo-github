# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

c = int(input("сколько лежит монет: "))
rever = aver = 0
for i in range(c):
    k = int(input("Введите 1 /орёл/ или 0 /решка/: "))
    if k > 1:
        print("Вы ввели неверное число.")
        k = int(input("Введите верное /1 или 0/: "))
    elif k == 1:
        rever += 1
    elif k == 0:
        aver += 1

if rever < aver:
    print(f'{rever}')
elif rever > aver:
    print(f' {aver}')
else:
    print(c // 2)

# c = int(input("сколько лежит монет: "))
# n = 0
# for i in range(c):
#     k = int(input("Введите 1/орёл/ или 0/решка/: "))
#     if k > 1:
#         print('Вы ввели неверное число')
#         k = int(input("Введите 1 или 0: "))
#     elif k == 1:
#         n += 1
#
# if n < c / 2:
#     print(n)
# else:
#     print(c - n)

