from random import randint
from easygui import *

def random_list(size):
    result =[]
    for _ in range(size):
        result.append(randint(1,100))
    return result

# print(random_list(10))
# print([randint(1,100) for _ in range(10)]) 


# второй список на основе первого, если элемент >0, то возвести в 2, иначе =0
# sp = [-5, 8, -9, 1, 7, 2]
# print([x for x in sp])
# print([x**2 for x in sp])
# print([x**2 for x in sp if x > 0])
# print([x**2 if x > 0 else 0 for x in sp])

# print({str(x): x for x in sp})
# print({str(i): randint(1,100) for i in range(10)})

size = int(enterbox("введите размер"))
msgbox(str({str(i): randint(1,100) for i in range(size)}))
# msgbox("Hello, world")



### Champ ###

# n = int(input()) 
# game = []  # формируем список состоявшихся игр 
# team = set()  # множество команд 
 
# while n > 0: 
#     str = input().split(';') 
#     team.update(set(str[::2])) 
#     game.append(str) 
#     n -= 1 
# # формируем турнирную таблицу 
# tbl = {} 
# for i in team: 
#     tbl[i] = [0, 0, 0, 0, 0] 
 
# for game_one in game: 
#     # кол-во проведенных игр 
#     tbl[game_one[0]][0] += 1 
#     tbl[game_one[2]][0] += 1 
 
#     if game_one[1] < game_one[3]: 
#         tbl[game_one[2]][3] += 1  # 1 команда проиграла 
#         tbl[game_one[0]][1] += 1  # 2 команда выиграла 
#     elif game_one[1] > game_one[3]: 
#         tbl[game_one[2]][1] += 1  # 1 команда выиграла 
#         tbl[game_one[0]][3] += 1  # 2 команда проиграла 
 
#     elif game_one[1] < game_one[3]: 
#         tbl[game_one[2]][3] += 1  # 1 команда проиграла 
#         tbl[game_one[0]][1] += 1  # 2 команда выиграла 
 
# for k in tbl: 
#     tbl[k][4] = tbl[k][1] * 3 + tbl[k][2] * 1 
#     print(k, end="") 
#     print(":", end="") 
#     for i in tbl[k]: 
#         print(i, end=" ") 
#     print()