# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.


def showContacts(phonebook):                # Просмотр списка контактов
    with open(phonebook, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("\n--- нажмите клавишу ВВОД ---")


def addContact(phonebook):                  # Добавление нового контакта
    with open(phonebook, "a", encoding="UTF-8") as file:
        record_line = ""
        record_line += input("Введите Фамилию контакта: ") + ","
        record_line += input("Введите Имя контакта: ") + ","
        record_line += input("Введите номер телефона контакта: ") + ","
        record_line += input("Введите город проживания контакта: ") + ","
        record_line += input("Введите степень знакомства с контактом: ")

        file.write(record_line + "\n")
    input("\nКонтакт добавлен!\n--- нажмите клавишу ВВОД ---")


def findContact(phonebook):                              # Поиск контакта
    target = input("Введите известные данные для поиска: ")
    result = []
    with open(phonebook, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)

    if len(result) != 0:
        printData(result)
    else:
        print(f"Контакта с такими данными в списках нет '{target}'.")

    input("--- нажмите клавишу ВВОД ---")


def changeContact(phonebook):                           # Изменение контакта
    with open(phonebook, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер контакта для изменения или 0 для возврата: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Введите новую фамилию: ")
            newName = input("Введите новое имя: ")
            newPhone = input("Введите новый номер: ")
            newcity = input("Введите новое место проживания: ")
            newstatus = input("Введите статус контакта: ")
            data[numberContact - 1] = (
                newLastName + "," + newName + "," + newPhone + "," + newcity + "," + newstatus + "\n"
            )
            with open(phonebook, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nДанные контакта изменены!")
                input("\n--- нажмите клавишу ВВОД ---")
        else:
            return


def deleteContact(phonebook):                             # Удаление контакта
    with open(phonebook, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(input("Введите номер для удаления или 0 для возврата: "))
        if numberContact != 0:
            print(f"Данные {data[numberContact-1].rstrip().split(',')} удалены\n")
            data.pop(numberContact - 1)
            with open(phonebook, "w", encoding="UTF-8") as file:
                file.write("".join(data))
        else:
            return

    input("--- нажмите клавишу ВВОД ---")


def printData(data):  # Вывод данных
    phoneBook = []
    splitLine = "=" * 90
    print(splitLine)
    print(" №  Фамилия         Имя           Номер Телефона   Место проживания   Степень знакомства")
    print(splitLine)
    personID = 1

    for contact in data:
        lastName, name, phone, city, status = contact.rstrip().split(",")
        phoneBook.append(
            {   "ID": personID,
                "lastName": lastName,
                "name": name,
                "phone": phone,  
                "city": city,
                "status": status
            }
        )
        personID += 1

    for contact in phoneBook:
        personID, lastName, name, phone, city, status = contact.values()
        print(f"{personID:>2}. {lastName:<15} {name:<10} - {phone:<16}  {city:<18} {status:<10}")

    print(splitLine)

def drawInterface():  # Рисование
    print("***  ТЕЛЕФОННАЯ КНИГА  ***")
    print("=" * 32)
    print(" [1] -- Список контактов")
    print(" [2] -- Добавить контакт")
    print(" [3] -- Найти контакт")
    print(" [4] -- Изменить данные контакта")
    print(" [5] -- Удалить контакт")
    print("\n [0] -- Выход")
    print("=" * 32)

def main(file_name):  # Меню
    while True:
        drawInterface()
        userChoice = int(input("Выберите пункт меню от 1 до 5 или 0: "))

        if userChoice == 1:
            showContacts(file_name)
        elif userChoice == 2:
            addContact(file_name)
        elif userChoice == 3:
            findContact(file_name)
        elif userChoice == 4:
            changeContact(file_name)
        elif userChoice == 5:
            deleteContact(file_name)
        elif userChoice == 0:
            print("удачных звонков!")
            return

main("phonebook.txt")