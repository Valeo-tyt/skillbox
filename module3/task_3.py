def f3():
    print('Задача 3. Следующее и предыдущее числа')
    inp = int(input('Введите целое положительное число: '))
    resp = inp // inp
    print('После числа', inp, 'идёт число', inp + resp)
    print('До числа', inp, 'идёт число', inp - resp)
