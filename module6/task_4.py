def f4():
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
