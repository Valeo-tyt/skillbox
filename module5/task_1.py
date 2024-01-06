def f1():
    lvl: int = 1
    experience = int(input("Введите полученное число очков опыта: "))
    if experience >= 5000:
        lvl += 3
    elif experience >= 2500:
        lvl += 2
    elif experience >= 1000:
        lvl += 1

    print("Уровень персонажа:", lvl)
