def f8():
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

