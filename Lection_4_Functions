### def ###

# def f(x):
#     return x*x

# print(f(5))
# print(type(f))
# a = f
# print(a(5))

### lambda #######

# def calc1(a, b):
#     return(a + b)

# def calc2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# calc3 = lambda a,b: a * b

# math(calc2, 5, 45)

# print(calc1(5, 45))

# math(calc3, 5, 45)

# math(lambda a,b: a + b, 5, 45)

###   > task <  ##

# в списке хранятся числа. нужно выбрать только чётные и составить список пар (числож квадрат числа)
# напр: 1 2 3 5 8 15 23 38
# result: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res. append((i, i**2))

# print(res)

## for -> lambda ##

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]

# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))

## select -> map ##
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

## where -> filter ##

# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


### map ##############

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x+10, list_1))
# print(list_1)

### filter #########

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

### > .split < ##################

# С клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел. 
# Этот набор чисел будет считан в качестве строки.
# Как превратить List строк в List чисел?

# data = '15 156 96 3 5 8 52 5'
# print(data)

# # data = data.split()
# # print(data)

# data = list(map(int, data.split()))
# print(data)

##  > zip < ##

# zip ([1, 2, 3, 4, 0], [7, 8, 9, 5], [Ы, Й, Ь])
# print(zip)

###  > enumerate < ##

data_s = (['Казань', 'Смоленск', 'Рыбинск', 'Чикаго'])
data - list(enumerate(data_s))
print(data)
[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбинск'), (3, 'Чикаго')]


