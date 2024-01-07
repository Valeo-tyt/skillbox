def f7():
    time = int(input('Введите время получения посылки: '))

    if time < 8 or time >= 22 or (14 <= time < 15) or (10 <= time < 12) or (18 <= time < 20):
        print("Посылку получить нельзя")


def f8():
    time = int(input('Введите время получения посылки: '))

    if (8 <= time < 10) or (12 <= time < 14) or (15 <= time < 18) or (20 <= time < 22):
        print("Посылку получить можно")
