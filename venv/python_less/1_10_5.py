a = int(input())
b = int(input())
h = int(input())

if h >= a:
    if h <= b:
        print('Это нормально')
    else:
        print('Пересып')
else:
    print('Недосып')
