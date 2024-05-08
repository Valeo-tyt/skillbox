def fine1():
    print('Задание 2.1 Система расчёта штрафов' + '\n')

    car_speed = 111
    is_town = True

    fine_for_1_to_10 = 30
    fine_for_11_to_15 = 50
    fine_for_16_to_20 = 70
    fine_for_21_to_25 = 115
    fine_for_26_to_30 = 180
    fine_for_31_to_40 = 260
    fine_for_41_to_50 = 400
    fine_for_51_to_60 = 560
    fine_for_61_to_70 = 700
    fine_for_70_and_more = 800

    town_speed = 50
    country_speed = 90
    result_fine = 0

    over_speed = car_speed - town_speed if is_town else car_speed - country_speed

    print('::' + str(over_speed) + '\n')  # Вывод фактического превышения

    if 1 < over_speed < 10:
        result_fine = fine_for_1_to_10
    elif 11 <= over_speed < 15:
        result_fine = fine_for_11_to_15
    elif 16 <= over_speed < 20:
        result_fine = fine_for_16_to_20
    elif 21 <= over_speed < 25:
        result_fine = fine_for_21_to_25
    elif 26 <= over_speed < 30:
        result_fine = fine_for_26_to_30
    elif 31 <= over_speed < 40:
        result_fine = fine_for_31_to_40
    elif 41 <= over_speed < 50:
        result_fine = fine_for_41_to_50
    elif 51 <= over_speed < 60:
        result_fine = fine_for_51_to_60
    elif 61 <= over_speed < 70:
        result_fine = fine_for_61_to_70
    elif over_speed >= 71:
        result_fine = fine_for_70_and_more

    if result_fine > 0:
        print("Штраф: " + str(result_fine) + '\n')
    else:
        print("Скорость не превышена или превышена незначительно" + '\n')


def fine2():
    print('--------------------------------------------------' + '\n')
    print('Задание 2.2 Система расчёта штрафов' + '\n')

    car_speed = 121
    is_town = True
    is_camera = False

    fine_for_20_to_40 = 500
    fine_for_40_to_60 = 1000
    fine_for_60_to_80 = 2000
    fine_for_80_and_more = 5000

    town_speed = 60
    country_speed = 90
    result_fine = 0

    if is_town:
        over_speed = car_speed - town_speed
    else:
        over_speed = car_speed - country_speed

    print('::' + str(over_speed) + '\n')  # Вывод фактического превышения

    if 20 <= over_speed < 40:
        result_fine = fine_for_20_to_40
    elif 40 <= over_speed < 60:
        result_fine = fine_for_40_to_60
    elif 60 <= over_speed < 80:
        result_fine = fine_for_60_to_80
    elif over_speed >= 80:
        result_fine = fine_for_80_and_more

    if result_fine > 20:
        print("Штраф: " + str(result_fine))
    else:
        print("Скорость не превышена или превышена незначительно")

    if not is_camera:
        if over_speed > 60:
            print('Лишение водительских прав')
        else:
            print('Превышение скорости зафиксировал инспектор')
    else:
        print('Превышение скорости зафиксировала камера')