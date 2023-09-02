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



# import sized as sized
# n = 384438
# m = str(n)
# left = int(m[0]) + int(m[1]) + int(m[2])
# right = int(m[3]) + int(m[4]) + int(m[5])
# if left == right:
#     print('yes')
# else:
#     print('no')