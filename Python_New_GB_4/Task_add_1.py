# задача 1 необязательная.
# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени,
# где все коэффициенты случайные от -10 до 10.
#
# например, k=2 ->       -x^2 + 3*x - 8 = 0    тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3      - 2*x = 0        тут коэффициенты  3,0,-2,0

import random

k = int(input("Введите коэффициент x: "))
str_out = ""
kk = []
while k > 0:
    k_ran = random.randint(-1, 1)
    if k_ran == 0:        
        str_out += ''
    elif k_ran == 1:
        str_out += '+' + 'x^' + str(k)
    elif k_ran == -1:
        str_out += '-' + 'x^' + str(k)
    elif k_ran < 0:
        str_out += str(k_ran) + '*' + 'x^' + str(k)
    elif k_ran > 0:
        str_out += '+' + str(k_ran) + '*' + 'x^' + str(k)
    kk.append(k_ran)
    k -= 1

k_ran = random.randint(-10, 10)
kk.append(k_ran)
if k_ran < 0:
    str_out += str(k_ran)
elif k_ran > 0:
    str_out += '+' + str(k_ran)

if str_out[0] == '+':
    str_out = str_out[1: ]

print(str_out)
print(f"коэффициенты: {kk}")

