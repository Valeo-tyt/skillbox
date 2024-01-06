def f2():
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