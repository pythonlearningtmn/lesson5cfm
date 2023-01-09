"""
Программа "Банковский счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""

import os
def bank_acc():
    balans = 0.0
    balans_read = ''
    history_orders = ''
    if os.path.exists('balans.txt'):
        with open('balans.txt', 'r') as b:
            balans_read = b.read()
            balans = 0.0 if balans_read == '' else float(balans_read)
    if os.path.exists('history.txt'):
        with open('history.txt', 'r') as h:
            history_orders = h.read()
    while True:
        print('\n1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню - ')
        if choice == '1':
            deposit = float(input('\nВведите сумму на сколько пополнить счет --> '))
            balans = balans + deposit if deposit > 0 else balans
            print(f'На Вашем счёте --> {balans} у.е.')
        elif choice == '2':
            purchase = float(input('\nВведите сумму покупки --> '))
            if purchase > 0:
                if balans >= purchase:
                    balans -= purchase
                    name_goods = input('Введите название покупки (наименование товара) --> ')
                    history_orders += (name_goods + ' ' + str(purchase) + '\n')
                else:
                    print('Недостаточно средств на счёте')
            print(f'На Вашем счёте --> {balans} у.е.')
        elif choice == '3':
            print('\nИстория покупок')
            print(history_orders)
        elif choice == '4':
            with open('balans.txt', 'w') as b:
                b.write(str(balans))
            with open('history.txt', 'w') as h:
                h.write(history_orders)
            break
        else:
            print('Неверный пункт меню')
