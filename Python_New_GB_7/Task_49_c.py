# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
# Напишите функцию find_farthest_orbit(list_of_orbits), которая 
# найдет среди списка орбит планет ту, по которой вращается самая далекая планета. 
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато 
# искусственные спутники были запущены на круговые орбиты. 
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
# При решении задачи используйте списочные выражения. 
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
# а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10


import math

def find_farest_orbits(list_of_orbits):
    index_gross_orbit = 0
    res = 0
    for i in range(len(list_of_orbits)):
        if list_of_orbits[i][0] != list_of_orbits[i][1]:            #  исключ круговых
            s = math.pi * list_of_orbits[i][0] * list_of_orbits[i][1]    #  вычисл орбит
            if s > res:                                             #  нахождение наибольшей
                res = s
                index_gross_orbit = i                               #  регистрация индекса наибольшей орбиты

    return index_gross_orbit


list_orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# print(find_farest_orbits(list_orbits))

def find_farest_orbits(list_of_orbits):
                       # вычисление площади /if/ НЕкруговых орбит  /из/ списка
    S = list(map(lambda x: math.pi * x[0]*x[1] if x[0] != x[1] else 0, list_of_orbits))  
    return S.index(max(S))

# list_orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(find_farest_orbits(list_orbits), list_orbits[find_farest_orbits(list_orbits)])


areas = [item[0]*item[1]*math.pi if item[0] != item[1] else 0 for item in list_orbits]
# print(areas.index(max(areas)))

