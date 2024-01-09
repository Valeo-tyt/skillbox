def f8():
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
