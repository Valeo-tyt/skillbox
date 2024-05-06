def f6_1():
    num = int(input('Введите число: '))
    count = 1
    while count <= num:
        print(count ** 3)
        count += 1


def f6_2():
    credit = int(input('Введите сумму долга: '))
    name = str(input('Введите ваше имя: '))

    print(name, f"ваша задолженность составляет {credit} рублей.", sep=", ")

    while True:
        summ = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
        if summ < credit:
            print(f"Маловато, {name}. Давайте ещё раз.")
        else:
            break
    print(f"Отлично, {name}! Вы погасили долг. Спасибо!")


def f6_3():
    number = int(input('Введите большое число: '))
    count = 0

    while True:
        number //= 10
        count += 1
        if number == 0:
            break
    print("Количество цифр в введённом числе:", count)


def f6_4():
    plus, minus = 0, 0

    while True:
        number = int(input('Введите число: '))
        if number < 0:
            minus += 1
        elif number > 0:
            plus += 1
        else:
            break

    print("Кол-во положительных чисел:", plus)
    print("Кол-во отрицательных чисел:", minus)


def f6_5():
    call_from_wife = False
    iterate, summ_task = 1, 0

    print("Начался восьмичасовой рабочий день.")
    while iterate <= 8:
        print(f"{iterate}-й час")
        iterate += 1
        task = int(input('Сколько задач решит Максим? '))
        summ_task += task
        call = int(input("Звонит жена. Взять трубку?"))
        if call == 1:
            call_from_wife = True

    print("Рабочий день закончился. Всего выполнено задач:", summ_task)
    if call_from_wife:
        print("Нужно зайти в магазин.")


def f6_6():
    deposit = int(input('Вклад в банке: '))
    percent = int(input('Величина годового процента: '))
    final_summ = int(input('Ожидаемая величина дохода: '))
    bank, year = 0, 1

    bank += deposit
    while True:
        bank += int(bank * (percent / 100))
        if final_summ <= bank:
            break
        else:
            year += 1
    print(f"При вкладе {deposit}р. с процентной ставкой {percent}% годовых, "
          f"для сбора суммы в {final_summ}р. нужно "
          f"копить {year} лет (год/а)")


def f6_7():
    hidden_number, iterate = 7, 1

    while True:
        number = int(input('Введите число: '))
        if number < hidden_number:
            print("Число меньше, чем нужно. Попробуйте ещё раз!")
            iterate += 1
        elif number > hidden_number:
            print("Число больше, чем нужно. Попробуйте ещё раз!")
            iterate += 1
        elif number == hidden_number:
            print("Вы угадали!")
            break
    print("Число попыток:", iterate)


def f6_8():
    maximum = 100
    minimum = 1

    while True:
        average = int((maximum + minimum) / 2)

        msg = int(input(f'Твоё число равно, меньше или больше, чем число {round(average)}: '))
        if msg == 2:
            minimum = average
            continue
        elif msg == 3:
            maximum = average
            continue
        else:
            break

    print("Загаданное число -", average)
