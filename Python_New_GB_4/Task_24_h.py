# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль, находясь непосредственно перед некоторым кустом, за один заход собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое за один заход собирающий модуль может собрать, 
# находясь перед некоторым кустом заданной во входном списке урожайности грядки.


import random
bush = int(input("введите количество кустов: "))
productivity = int(input("введите урожайность грядки: "))
berryes = list(random.randint(0, productivity//bush) for i in range(bush))
print(berryes)

harvest = []
i = 0
sum = 0

while (i < bush):
    if (i == bush - 1):
        sum = berryes[i] + berryes[i - 1] + berryes[0]
    else:
        sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
    harvest.append(sum)
    harvest.sort()
    i += 1


print(f"максимальное число ягод за один подход {harvest[-1]}")