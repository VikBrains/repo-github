# def Summa(num1: int, num2: int) -> int:
#     if not isinstance(num1, int):
#         #raise ValueError("This must be a integer")
#     #return num1 + num2
#
# print(Summa(1,3))
# print(Summa("Hi", " all "))

# Пользователь вводит натуральное k.
# Надо сформировать многочлен такой степени, где все коэффициенты случайные от -10 до 10.
#
# например, k=2 -> -x^2 + 3*x - 8 = 0  # тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0     # тут коэффициенты 3,0,-2,0

from random import randint

k = int(input("Введите натуральное число: "))

a = randint(-10,10)
b = randint(-10,10)
c = randint(-10,10)


print.Join("{a}, *, x, ^, {k}, {b}, *, x, {c}")