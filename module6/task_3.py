def f3():
    number = int(input('Введите большое число: '))
    count = 0

    while True:
        number //= 10
        count += 1
        if number == 0:
            break
    print("Колличество цифр в введённом числе:", count)
