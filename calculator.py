while True:
    a = int(input('Введите первое число: '))
    c = input('Выберите операцию +, -, *, /: ')
    b = int(input('Введите второе число: '))

    if c == '+':
        print(a + b)

    elif c == '-':
        print(a - b)

    elif c == '*':
        print(a * b)

    elif c == '/':
        if b == 0:
            print('На 0 делить нельзя')
        else:
            print(a / b)

    else:
        print('Вы ввели некорректный символ')

    e = input('Желаете продолжить, если да, то нажмите любую клавишу, если нет, то нажмите ".": ')
    
    if e == '.':
        break
