def f1():
    client = 'Петя'
    pet = 'Кот'
    print(client)
    print(' и ')
    print(pet)


def f2():
    r = 'Red'
    g = 'Green'
    b = 'Blue'
    print(r, b, g, r + g + b, b, g + b)


def f3():
    first_animal = input('Введите первое животное: ')
    second_animal = input('Ведите второе животное: ')
    print(first_animal + ' спит, ' + second_animal + ' идёт')


def f4():
    name = input('Введите имя пользователя: ')
    print('Привет, ' + name)
    prefix_msg = 'К сожалению, у Вас нет доступа к системе.'
    postfix_msg = 'Пожалуйста, обратитесь к системному администратору.'
    print(prefix_msg + '\n' + postfix_msg)


def f5():
    city_departure = input('Введите город вылета: ')
    city_arrival = input('Введите город прилёта: ')
    print(city_departure, '-', city_arrival)


def f6():
    a = input('Введите первое слово: ')
    b = input('Введите второе слово: ')
    print(a, b)
    c = a
    a = b
    b = c
    print(a, b)
