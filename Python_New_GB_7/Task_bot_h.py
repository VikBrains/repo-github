# Задача ДОП по желанию Сделать свой локальный чат-бот 
# аналогично приложенной записи (ниже).

# # # К сожалению, бот из записи не заработал, (json - файл)

from random import *
import json
films=[]
# films.append("Матрица")
# films.append("Солярис")
# films.append("Властелин Колец")
# films.append("Техасская резня бензопилой")
# films.append("Санта-Барбара")

def save():
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dump(films, ensure_ascii = False))
    print("наша фильмотека была успешно сохранена в файле films.json")

def load():
    with open("films.json", "r", encoding="utf-8") as fh:
        films=json.load(fh)
    print("Фильмотека была успешно загружена")

try:
    load()
except:
    films=[]
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властелин Колец")
    films.append("Техасская резня бензопилой")
    films.append("Санта-Барбара")


while True:
    command = input("Введите команду: ")
    if command == "/start":
        print("Бот-фильмотека начал свою работу")
    elif command == "/all":
        print("Текущий список фильмов")
        print(films)
    elif command == "/add":
        f=input("Введите название фильма: ")
        films.append(f)
        print("Фильм был успешно добавлен в коллекцию")
    elif command =="/help":
        print("Здесь какой-то мануал")
    elif command == "/random":
        #rnd = randint(0, len(films)-1)
        #print("Жребий выбрал для Вас фильм - " + films[rnd])
        print("Жребий выбрал для Вас фильм - " + choice(films))
    elif command == "/delete":
        f=input("введите название фильма, который нужно удалить: ")

        # if f in films:
        #     films.remove(f)
        #     print("Фильм был успешно удалён")
        # else:
        #     print("Такого фильма у нас нет!")
        try:
            films.remove(f)
            print("Фильм был успешно удалён")
        except:
            print("Такого фильма у нас нет!")

    elif command == "/save":
        save()
    elif command == "/load":
        load()
    elif command == "/stop":
        print("Бот остановил свою работу. Заходите ещё, будем рады")
        break
    else:
        print("Неопознанная команда. Просьба погладить Манула через /help")


