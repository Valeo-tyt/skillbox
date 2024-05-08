def f7_1():
    condition_number = 0
    for count in range(10):
        number = int(input('Введите число для анализа:'))
        if number > 0 and number % 2 == 0:
            condition_number += 1
    print("Положительных чётных чисел -", condition_number)


def f7_2():
    total_salary = 0
    for mount in range(12):
        salary = int(input("Введите зарплату за текущий месяц:"))
        total_salary += salary
    average_salary = total_salary / 12
    print("Средняя зарплата в месяц:", average_salary)


def f7_3():
    factorial = 1
    number = int(input("Введите число:"))
    for count in range(1, (number + 1)):
        factorial = factorial * count
    print(factorial)


def f7_4():
    very_good, good, normal = 0, 0, 0
    total_users = int(input("Введите кол-во учеников в классе:"))
    for count in range(total_users):
        mark = int(input(f"Ученик {count+1} получил оценку:"))
        if mark == 3:
            normal += 1
        elif mark == 4:
            good += 1
        elif mark == 5:
            very_good += 1
        else:
            print("Противоречит условию")
    print(f"В классе отличников - {very_good}, хорошистов - {good}, троечников - {normal}")


def f7_5():
    number_a = int(input("Введите первое число:"))
    number_b = int(input("Введите второе число:"))
    result, index = 0, 0
    for counter in range(number_a, (number_b+1)):
        if counter % 3 == 0:
            result += counter
            index += 1
    output = result / index
    print(f"Среднее арифметическое чисел из отрезка {number_a} и {number_b} кратных трём равно", output)


def f7_6():
    for num in range(10, 100):
        digit1 = num // 10
        digit2 = num % 10
        product = digit1 * digit2 * 3

        if num == product:
            print(num)


def f7_7():
    total_cards = int(input("Введите количество карточек:"))
    presence_sheet: list = []
    for index in range(1, total_cards):
        card = int(input("Введите номер оставшейся карточки:"))
        presence_sheet.append(card)
    for card in range(1, total_cards + 1):
        if card not in presence_sheet:
            print("Номер пропавшей карточки:", card)

