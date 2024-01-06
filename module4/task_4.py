def f4():
    product1 = int(input("Введите стоимость первого товара: "))
    product2 = int(input("Введите стоимость второго товара: "))
    product3 = int(input("Введите стоимость третьего товара: "))
    total_amount = product1 + product2 + product3
    bank = 10000
    if total_amount >= bank:
        total_amount -= total_amount * 0.1
        print("Итоговая сумма:", int(total_amount))
    else:
        print("Итоговая сумма:", int(total_amount))
