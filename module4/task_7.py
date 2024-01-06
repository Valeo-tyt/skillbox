def f7():
    hours = int(input("Введите кол-во часов: "))
    credit = int(input("Остаток по кредиту: "))
    bank = int(input("Остаток на еду: "))
    salary = 200 * hours / 2 ** 3 + hours
    expense = credit + bank
    if salary-expense >= 0:
        print("Часов хватает. Можно отдохнуть")
    else:
        print("Часов не хватает. Придётся работать больше!")
