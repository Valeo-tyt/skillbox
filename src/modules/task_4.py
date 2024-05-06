def f4_1():
    quest = int(input("На улице идёт дождь?: "))
    if quest == 1:
        print("Пошёл дождь. Возьмите зонтик!")
    else:
        print("Дождя нет!")


def f4_2():
    undaid = 270

    rus = int(input("Введите количество баллов по русскому языку: "))
    mathm = int(input("Введите количество баллов по математике: "))
    infor = int(input("Введите количество баллов по информатике: "))

    if (rus + mathm + infor) >= undaid:
        print("Поздравляю, ты поступил на бюджет!")
    else:
        print("К сожалению, ты не прошёл на бюджет.")


def f4_3():
    day = int(input("Введите сегодняшнее число: "))
    day %= 2
    if day != 0:
        print("Сегодня не чётное число!")
    else:
        print("Сегодня чётное число!")


def f4_4():
    product1 = int(input("Введите стоимость первого товара: "))
    product2 = int(input("Введите стоимость второго товара: "))
    product3 = int(input("Введите стоимость третьего товара: "))
    total_amount = product1 + product2 + product3
    bank = 10000
    if total_amount >= bank:
        total_amount -= total_amount * 0.1
        print("Итоговая сумма:", int(total_amount))
    else:
        print("Итоговая сумма:", int(total_amount))


def f4_5():
    count = int(input("Введите число: "))
    print(abs(count))


def f4_6():
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    if number1 >= number2:
        print("Разность:", number1-number2)
        print("Игрок платит")
    else:
        print("Сумма:", number1+number2)
        print("Владелец платит")
    print("Игра окончена")


def f4_7():
    hours = int(input("Введите кол-во часов: "))
    credit = int(input("Остаток по кредиту: "))
    bank = int(input("Остаток на еду: "))
    salary = 200 * hours / 2 ** 3 + hours
    expense = credit + bank
    if salary-expense >= 0:
        print("Часов хватает. Можно отдохнуть")
    else:
        print("Часов не хватает. Придётся работать больше!")


def f4_8():
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    number3 = int(input("Введите третье число: "))
    if number2 < number1 > number3:
        print("Первое число максимальное из трёх:", number1)
    elif number1 < number2 > number3:
        print("Второе число максимальное из трёх:", number2)
    elif number2 < number3 > number1:
        print("Третье число максимальное из трёх:", number3)
    else:
        print("Условия некорректны")
