sp = [55, 44, "hello", True, 99.88, 100]

# for i in range(len(sp)):
#     print(sp[i])                 # распечатка всего списка по индексам

# for item in sp:
#     print(item)                  # распечатка всего списка

# for i, value in enumerate(sp):
#     print(i, value)              # распечатка списка с индексами

# print("True" in sp)           # выведение ???

# sp.append("last")             # добавление к концу списка
# sp.insert(5,"zero")           # добавление в точку индекса
# sp.extend([1,2,3])            # расширение массива на указанные элементы
# sp += [1,2,3]*3               # расширение массива на указанные элементы указанное число раз
# print([None]*10)              # ???
# del sp[0]                     # Удаление элемента с указанным индексом
# sp.remove(True)               # Удаление указанного элемента
## a = sp.pop()                 # Удаление последнего элемента с -
## print(a)                     # - c выведением удалённого элемента
# print(sp)
# print(len(sp))                # Длина списка

# list tuple set dict           # ???
## t = (5,7,"privet")           # кортеж
## print(type(t))               # кортеж 
## print(t[2])                  # кортеж

# s = {88,888,8,8,8,8}          # массив оригинальных элементов
# print(s)                      # 
# s.add(777)                    # добавление к массиву указанного элемента 
# print(sp)                      # 
# s.discard(777)                # удаление из массива указанного
# print(s)                      #

d = {123: 4654454, "тетя ира": [45454]}
d["дядя ваня"] = "546545"
# d[input("Введите имя контакта ")] = input("Введите номер телефона ")       # ???
d["тетя ира"].append(55255)
# print(d)
# del d[123]
# print(d)
# print(d.keys())
# print(d.values())
# for k in d:
#     print(k)
for key, value in d.items():
    print(f"{key} - {value}")

