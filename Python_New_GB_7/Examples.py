from time import time

def how_long(func):
    start = time()
    func()
    print(f"на это ушло {time() - start} секунд")

def create_list():
    return[i for i in range(500000)]

# how_long(create_list)
def calc_power(pow):
    def calc_value(root):
        return root ** pow
    return calc_value

# print(calc_power(2)(3))  # 9
# square = calc_power(2)
# cube = calc_power(3)
# print(square(8))         # 64
# print(cube(2))           # 8

calc = {'+' : lambda x,y: x + y,
        '-' : lambda x,y: x - y,
        '*' : lambda x,y: x * y,
        '/' : lambda x,y: x / y}

# def obrab(x,y,calc):
#     for key in calc:
#         print(calc[key](x,y))

# print(calc['*'](9,4))
# obrab(7,4,calc)

sp = [7, 8, 11, -5, -9, -7]
sp2 = ["Иван", "Коля"]

# print(type(sp))
# print(sp)
# print(*sp)
# print(list(map(abs, sp)))
# print(*map(abs, sp))
# print(*map(lambda item: -item, sp))
# print(*map(lambda item: item**2 if item > 0 else 0, sp))

# print(*filter(lambda item: item > 0, sp))

# for item in zip(sp, sp2):
    # print(item)

### DOP  ###

# Необходимо написать программу для автоматического перевода различных валютных счетов в рублевые.
# Начальные данные программы это три различных списка 
# - Фамилии владельцев банковских счетов, 
# - указание валют счетов, 
# - соответствующее состояние счетов.   То есть у Иголкина счет в евро и там лежит 50000, и так далее.
# Также вначале заданы отношения курса рубля к доллару и евро.
# Вам необходимо написать функцию calc, которая на входе принимает только один аргумент, далее надо применить ее в комбинациях с map и zip.
# На выходе программы должны быть три пары значений - фамилии владельцев счетов и состояние рублевого счета.    

def calc(people_money):
#    res = list(map(lambda x: (x[0],x[2]*dollar) if x[1] == "доллар" ??? else (x[0],x[2]), people_money))
    res = people_money[1]
    if people_money[0] == "доллар":
        res *= dollar
    elif people_money[0] == "евро":
        res *= euro
    return res

surnames = ["Иванов", "Карпов", "Иголкин"]
currency_name = ["рубль", "доллар", "евро"]
balances = [30000, 40000, 50000]
dollar = 90
euro = 99

# people_money = list(zip(surnames, currency_name, balances))
new_balances = list(map(calc, zip(currency_name, balances)))
# print(people_money)
# print(calc(people_money))
print(*zip(surnames, new_balances))
