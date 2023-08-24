name = str(input('Введите имя: '))

# Определяем функцию, чтобы проверить, содержит ли имя гласную букву
def has_vowel():
    if set('аеёиоуыэюя').intersection(name.lower()):
        print('Имя содержит гласную.')
    else:
        print('Имя не содержит гласную.')

# Итерация по буквам в строке имени
def print_letters():
    for letter in name:
        print(letter)

def main():
    has_vowel()
    print_letters()

# Выполняем функцию main()
if __name__ == '__main__':
    main()
