# Задача №25. Общее обсуждение
# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Для решения данной задачи используйте функцию .split()

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

def Get_Count_Letter(sp):
    sp1 = sp.split()
    lib = {}
    sp_out = []
    for i in sp1:
        if i in lib:
            sp_out.append(i + "_" + str(lib[i]))
            lib[i] = lib[i] + 1
        else:
            lib[i] = 1
            sp_out.append(i)
    return sp_out


sp = "a a a b c a a d c d d"
print(Get_Count_Letter(sp))


# word = input("Введите строку: ")

# st = "a a a b c a a d c d d"
# st1 = st.split()
#
# for i in st1:
#     for j in st1:
#         count = 1
#         if i == j:
#             st1 = { }
#             j = j + str(count)
#
#
#
#             count =+ 1
#
# print(st1)
