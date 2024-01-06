def f7():
    number = int(input('Введите положительное целое четырёхзначное число : '))
    thousands = number // 1000
    hundreds = number // 100 % 10
    tens = number % 100 // 10
    units = number % 10
    print(thousands, hundreds, tens, units)
