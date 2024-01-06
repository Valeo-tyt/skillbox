def f5():
    print('Задача 5. Часы')
    minutes = int(input('Введите колличество минут: '))
    if minutes < 60:
        print('Ваше время составляет:', minutes, 'минут.')
    else:
        hours = minutes // 60
        minute = minutes % 60
        print('Ваше время составляет:', hours, 'час(а/ов),', minute, 'минут.')
