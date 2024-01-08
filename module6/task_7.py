def f7():
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
