def f5_1():
    lvl: int = 1
    experience = int(input("Введите полученное число очков опыта: "))
    if experience >= 5000:
        lvl += 3
    elif experience >= 2500:
        lvl += 2
    elif experience >= 1000:
        lvl += 1

    print("Уровень персонажа:", lvl)


def f5_2():
    x = int(input("Введите число икс: "))
    if x == 0:
        y = 5
    elif x < 0:
        y = x ** 2
    else:
        y = x - 12

    print("Игрек равен", y)


def f5_3():
    position = int(input("Введите место в списке поступающих: "))
    if position <= 10:
        point = int(input("Введите количество баллов за экзамены: "))
        if point >= 290:
            print("Поздравляем, вы поступили!")
            print("Бонусом вам будет начисляться стипендия.")
        else:
            print("Поздравляем, вы поступили!")
            print("Но вам не хватило баллов для стипендии.")
    else:
        print("К сожалению, вы не поступили.")


def f5_4():
    rating = int(input('Что получил по математике? '))
    if rating == 2 or rating == 3:
        print('Плохо. Марш учиться!')
    elif rating == 4 or rating == 5:
        print('Молодец! Можешь отдохнуть.')


def f5_5():
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    number3 = int(input('Введите третье число: '))

    if number1 == number2 and number2 == number3:
        print("3")
    elif number1 != number2 and number2 != number3 and number1 != number3:
        print("0")
    else:
        print("2")


def f5_6():
    flat = int(input('Введите число кв.м. квартиры: '))
    cost = int(input('Введите стоимость квартиры: '))

    if flat >= 100 and cost <= 10000000:
        print("Данный вариант (1) подходит для покупки")
    elif flat >= 80 and cost <= 7000000:
        print("Данный вариант (2) подходит для покупки")
    else:
        print("Введённая конфигурация не подходит под условия покупки")


def f5_7():
    time = int(input('Введите время получения посылки: '))

    if time < 8 or time >= 22 or (14 <= time < 15) or (10 <= time < 12) or (18 <= time < 20):
        print("Посылку получить нельзя")
    else:
        print("Посылку получить можно")


def f5_8():
    time = int(input('Введите время получения посылки: '))

    if (8 <= time < 10) or (12 <= time < 14) or (15 <= time < 18) or (20 <= time < 22):
        print("Посылку получить можно")
    else:
        print("Посылку получить нельзя")
