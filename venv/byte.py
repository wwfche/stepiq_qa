#print('hello')
#age = 26
#name = 'tratata'

#print('Возраст {} -- {} лет.'.format(name, age))
#print('Почему {0} забавляется с этим Python?'.format(name))

#i = 5
#print(i)
#i = i + 1
#print(i)

#s = '''Это коммунальная
#коммунальная
#квартира
#'''
#print(s)

#
# number = 23
# guess = int(input('Введите целое число : '))

#if guess == number:
#    print('Поздравляю, вы угадали число, ')
 #   print('(хотя и не выиграли приза)')
#
#elif guess < number:
 #   print('нет, загаданное число немного больше этого.')

#else:
 #   print('Нет, загаданное число немного меньше этого.')

#print('Завершено')

##
def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно ', b)
    else:
        print(b, 'максимально')

printMax(99, 100)

x = 1000
y = 1001

printMax(x, y)