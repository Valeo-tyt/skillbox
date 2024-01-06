def f2():
    x = int(input("Введите число икс: "))
    if x == 0:
        y = 5
    elif x < 0:
        y = x ** 2
    else:
        y = x - 12

    print("Игрек равен", y)
