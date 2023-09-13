# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# k = int(input('Введите число: '))
k = 8

def get_fibonacci(k):
    fibonacci_row = []

    a, b = 0, 1
    for i in range (k):
        fibonacci_row.insert(0, a)
        a, b = b, a - b

    a, b = 1, 1
    for i in range(k-1):
        fibonacci_row.append(a)
        a, b = b, a + b

    return fibonacci_row
print(get_fibonacci(k))


# def get_fibonacci(k):
#     fibonacci_row = []

#     a, b = 0, 1
#     for i in range(k):
#         a, b = b, a + b
#         fibonacci_row.append(a)

#     return fibonacci_row
 
# print(get_fibonacci(k))


# fibonacci = [0, 1]
# for i in range(k):
#     fibonacci.append((fibonacci[-2] + fibonacci[-1]))

# for i in range(k):
#     fibonacci.insert(0, fibonacci[-2] - fibonacci[-1])
 
# print(fibonacci)
