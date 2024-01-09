def f6():
    deposit = int(input('Вклад в банке: '))
    percent = int(input('Величина годового процента: '))
    final_summ = int(input('Ожидаемая величина дохода: '))
    bank, year = 0, 1

    bank += deposit
    while True:
        bank += int(bank * (percent / 100))
        if final_summ <= bank:
            break
        else:
            year += 1
    print(f"При вкладе {deposit}р. с процентной ставкой {percent}% годовых, "
          f"для сбора суммы в {final_summ}р. нужно "
          f"копить {year} лет (год/а)")
