# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
#    (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
 
import json

sp = {'Николай': {'Номер' : ['7-965-841-23-05', '7-951-248-63-84'], 'Город' : 'Урюпинск', 'Статус' : 
'дядя'}, 'Анна' : {'Номер' : ['7-953-476-21-58'], 'Город' : 'Волжск', 'Статус' : 'сестра'}}

while True:
    command = input('Введите команду: ')
    if command == '/all':
        print('Текущий список контактов')
        for k, v in sp.items():
            print(k, v)

    elif command == '/add.contact':
        name = input('Введите имя нового Контакта: ')
        if name in sp:
            print('Контакт уже существует')
        else:
            coll = int(input('Сколько номеров Вы хотите ввести?: '))
            phones = []
            for i in range(coll):
                numbers = input('Введите следующий номер: ')
                phones.append(numbers)
                coll -= 1
            city = input('Введите название города: ')
            status = input('Введите сведения о контакте: ')
            sp[name] = {'номер телефона': numbers, 'город': city, 'Status': status}  

# with open(phonebook, "a", encoding="UTF-8") as file:
#         res = ""
#         res += input("Введите Фамилию контакта: ") + ","
#         res += input("Введите Имя контакта: ") + ","
#         res += input("Введите номер телефона контакта: ") + ","
#         res += input("Введите город проживания контакта: ") + ","
#         res += input("Введите степень знакомства с контактом: ")

#         file.write(res + "\n")
#     input("\nКонтакт добавлен!\n--- нажмите клавишу ВВОД ---")



    elif command == '/add.number':
        name = input('Введите имя контакта: ')
        if name not in sp:
            print('Контакта нет в Вашем списке')
        else:
            phone = input('Введите номер: ')
            if phone in sp[name]['номер телефона']:
                print('Номер существует')
            else:
                sp[name]['номер телефона'].append(phone)



def save():
    with open("phonebook.json", "w", encoding="utf-8") as fb:
        fb.write(json.dump(phonebook, ensure_ascii = False))
    print("наша фильмотека была успешно сохранена в файле phonebook.json")

def load():
    with open("phonebook.json", "r", encoding="utf-8") as fh:
        phonebook=json.load(fh)
    print("Фильмотека была успешно загружена")

try:
    load()
except:
    phonebook=[]
    phonebook.append("Матрица")
    phonebook.append("Солярис")
    phonebook.append("Властелин Колец")



while True:
    command = input("Введите команду: ")
    if command == "/start":
        print("Бот-фильмотека начал свою работу")
    elif command == "/all":
        print("Текущий список фильмов")
        print(phonebook)
    elif command == "/add":
        f=input("Введите название фильма: ")
        phonebook.append(f)
        print("Фильм был успешно добавлен в коллекцию")
    elif command =="/help":
        print("Здесь какой-то мануал")
    elif command == "/random":
        #rnd = randint(0, len(phonebook)-1)
        #print("Жребий выбрал для Вас фильм - " + phonebook[rnd])
        print("Жребий выбрал для Вас фильм - " + choice(phonebook))
    elif command == "/delete":
        f=input("введите название фильма, который нужно удалить: ")

        try:
            phonebook.remove(f)
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


