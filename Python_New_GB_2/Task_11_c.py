# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не # является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6


def search_possition_number_in_Fibbonachi(number):
    num_fib = [0,1]                                    # Организация ряда Фибоначчи (4 строки)
    while number > num_fib[-1]:
        new_num_fib = num_fib[-1]+num_fib[-2]
        num_fib.append(new_num_fib)
    if num_fib[-1] == number:                          # Проверка принадлежности числа ряду Ф.
        return len(num_fib)                              # вывод индекса, если принадлежит
    return -1                                            # вывод индикатора НЕпринадлежности

try:
    number = int(input("Введите число: "))
    print(f"Позиция числа {number} в последовательности Фиббоначи "
          f"{search_possition_number_in_Fibbonachi(number)}")
except:
    print("Ввели неверные данные")

    # def fib_find(n):
    #     n1 = 0
    #     n2 = 1
    #     res = 0
    #     counter += 1
    #     while res < n:
    #         res = n1 + n2
    #         n1 + n2
    #         n2 = res
    #         counter += 1
    #     if res == n:
    #         return counter
    #     else:
    #         return (f"Вы ввели не число Фибоначчи. Ближайшее число {n1}")
    #
    # n = int(input('Введите число ->'))
    # print(fibonachi_find(n))
