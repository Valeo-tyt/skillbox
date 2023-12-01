def f6():
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    if number1 >= number2:
        print("Разность:", number1-number2)
        print("Игрок платит")
    else:
        print("Сумма:", number1+number2)
        print("Владелец платит")
    print("Игра окончена")
