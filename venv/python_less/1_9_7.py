a = int(input())
b = int(input())
if b != 0:
    print(a / b)
else:
    b = int(input('Введите повторно = '))
    if b == 0:
        print('ЛОХ')
    else:
        print(int(a / b))