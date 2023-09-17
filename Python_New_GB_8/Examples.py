# Телефонный Справочник

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

# phone_format(phone),

# def phone_format(n):  # формат номера
#     n = n.removeprefix("+")
#     n = re.sub("[ ()-]", "", n)
#     return format(int(n[:-1]), ",").replace(",", "-") + n[-1]