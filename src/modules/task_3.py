def f3_1():
    print('Задача 1. Язык математики')
    a, b, c, d = 8, 10, 12, 18
    numerator = (-3 + a ** 2) * b - 2 ** 3
    denominator = c - (2 * d)
    res = numerator / denominator
    print(res)


def f3_2():
    print('Задача 2. Финансовый отчёт')
    q1 = int(input('Введите сумму дохода за первый квартал: '))
    q2 = int(input('Введите сумму дохода за второй квартал: '))
    q3 = int(input('Введите сумму дохода за третий квартал: '))
    q4 = int(input('Введите сумму дохода за четвёртый квартал: '))
    response = (q1 + q2) / (q3 + q4)
    print('Динамика роста:', response)


def f3_3():
    print('Задача 3. Следующее и предыдущее числа')
    inp = int(input('Введите целое положительное число: '))
    resp = inp // inp
    print('После числа', inp, 'идёт число', inp + resp)
    print('До числа', inp, 'идёт число', inp - resp)


def f3_4():
    print('Задача 4. Площадь треугольника')
    leg_a = int(input('Введите длину катета "a": '))
    leg_b = int(input('Введите длину катета "b": '))
    s = (leg_a*leg_b)/2
    print('Площадь прямоугольного треугольника равна:', s)


def f3_5():
    print('Задача 5. Часы')
    minutes = int(input('Введите колличество минут: '))
    if minutes < 60:
        print('Ваше время составляет:', minutes, 'минут.')
    else:
        hours = minutes // 60
        minute = minutes % 60
        print('Ваше время составляет:', hours, 'час(а/ов),', minute, 'минут.')


def f3_6():
    print('Задача 6. Проверяем бухгалтера')
    print('Manual: Необходимо вводить положительное целое трёхзначное число (или с большей разрядностью)')
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    number_1 %= 100
    number_2 %= 100
    response: int = number_1 + number_2
    print('Сумма двух последних разрядов:', response)


def f3_7():
    number = int(input('Введите положительное целое четырёхзначное число : '))
    thousands = number // 1000
    hundreds = number // 100 % 10
    tens = number % 100 // 10
    units = number % 10
    print(thousands, hundreds, tens, units)


def f3_8():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print(a, b)
    a = a + b
    b = a - b
    a = a - b
    print(a, b)
