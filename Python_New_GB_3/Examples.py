# sp = [55, 44, "hello", True, 99.88, 100]

# for i in range(len(sp)):
#     print(sp[i])
#
# for item in sp:
#     print(item)
#
# for i, value in enumerate(sp):
#     print(i, value)

# print("hello" in sp)
#
# sp.append("last")
# sp.insert(0,"zero")
# sp.extend([1,2,3])
# sp += [1,2,3]*3
# print([None]*10)
# del sp[0]
# sp.remove(True)
# a =sp.pop()
# print(a)
# print(sp)
# print(len(sp))
# lest tuple set dict
# t = (5,7,"privet")
# print(type(t))
# print(t[0])
# s = {8,8,8,8,8,8,8,8,8}
# s add(777)
# s.discard(77777)
# print(a)
#
# d = {123: 4654454, "тетя ира": [45454,5555]}
# d["дядя ваня"] = "546545"
# d[input("Введите имя контакта ")] = input("Введите номер телефона ")
# d["тетя ира"].append(56465)
# # print(d)
# # del d[123]
# # print(d)
# # print(d.keys())
# # print(d.values())
# # for k in d:
# #     print(k)
# for key, value in d.items():
#     print(f"{key} - {value}")

#сколько раз встречается конкретная цифра в этом списке?
#sp = [55.1245, 44 ,"5ррууу55",   [95.45,0.5] , {53:  125} ]
#ответ будет 11 раз
#для цифры 5 в поиске
# sp = [55.1245, 44 ,"5ррууу55",   [95.45,0.5] , {53:  125} ]
#
# s=str(sp) #Преобразовали в строку
# #result=0
# #for sym in s: #По строке
# #    if sym==str(5):
# #        result+=1
#
# print(s.count("5"))

# #сколько раз встречается конкретная цифра в этом списке?
# #sp = [55.1245, 44 ,"5ррууу55",   [95.45,0.5] , {53:  125} ]
# #ответ будет 11 раз
# #для цифры 5 в поиске
# sp = [55.1245, 44 ,"5ррууу55",   [95.45,0.5] , {53:  125} ]
#
# s=str(sp) #Преобразовали в строку
# #result=0
# #for sym in s: #По строке
# #    if sym==str(5):
# #        result+=1
#
# print(s.count("5"))


# scr_price = {1:"AEIOULNSTRАВЕИНОРСТ",
#                 2:"DGДКЛМПУ",
#                 3:"BCMPБГЁЬЯ",
#                 4:"FHVWYЙЫ",
#                 5:"KЖЗХЦЧ",
#                 8:"JXШЭЮ",
#                 10:"QZФЩЪ"}
#
# word = input("Введите слово: ").upper()
# summ = 0
# for i in word:
#     for k, v in list_letters.items():
#         if i in v:
#             summ += k
# print(f"Стоимость слова: {summ}")

k = "ноутбук"
scr_price = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}
# scr_price = { 1:"AaEeIiOoUuLlNnSsTtRrАаВвУуИиНнОоРрСсТт",
#              2:"DdGgДдКкЛлМмПпУу",
#              3:"BbCcMmPpБбГгЁёЬьЯя",
#              4:"FfHhVvWwYyЙйЫы",
#              5:"KkЖжЗзХхЦцЧч",
#              8:"JjXxШшЭэЮю",
#             10:"QqZzФфЩщЪъ"}


sum = 0

for i in k:
    for x, v in scr_price.items():
        if i in v:
            sum += x
#     for k, v in Eng.items():
#         if i in v:
#             sum += k
print(f"{sum} очков")