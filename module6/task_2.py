def f2():
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
