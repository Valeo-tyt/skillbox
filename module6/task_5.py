def f5():
    call_from_wife = False
    iterate, summ_task = 1, 0

    print("Начался восьмичасовой рабочий день.")
    while iterate <= 8:
        print(f"{iterate}-й час")
        iterate += 1
        task = int(input('Сколько задач решит Максим? '))
        summ_task += task
        call = int(input("Звонит жена. Взять трубку?"))
        if call == 1:
            call_from_wife = True

    print("Рабочий день закончился. Всего выполнено задач:", summ_task)
    if call_from_wife:
        print("Нужно зайти в магазин.")
