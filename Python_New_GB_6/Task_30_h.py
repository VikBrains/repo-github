# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


array = []
a1 = int(input("введите 1ый элемент арифм. прогрессии: "))
d = int(input("введите разность арифм. прогрессии: "))
n = int(input("введите количество элементов прогрессии: "))

for i in range(n):
    ai = a1 + (i *d)
    array.append(ai)
    
print(array)