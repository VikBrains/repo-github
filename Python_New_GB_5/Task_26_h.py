# Задача 26: 
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

def pow_res(m, n):
    if n == 1:
        return m
    elif n == 0:
        return 1
    return m * pow_res(m, n - 1)

    
print(pow_res(a, b))

