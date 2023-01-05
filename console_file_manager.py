# Проект "Консольный файловый менеджер"
"""
1. Создать новый проект ""Консольный файловый менеджер"
2. В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.
Так же можно добавить любой дополнительный функционал по желанию.

Описание пунктов:
- создать папку
после выбора пользователь вводит название папки, создаем её в рабочей директории;
- удалить (файл/папку)
после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть;
- копировать (файл/папку)
после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;
- просмотр содержимого рабочей директории
вывод всех объектов в рабочей папке;
- посмотреть только папки
вывод только папок которые находятся в рабочей папке;
- посмотреть только файлы
вывод только файлов которые находятся в рабочей папке;
- просмотр информации об операционной системе
вывести информацию об операционной системе (можно использовать пример из 1-го урока);
- создатель программы
вывод информации о создателе программы;
- играть в викторину
запуск игры викторина из предыдущего дз;
- мой банковский счет
запуск программы для работы с банковским счетом из предыдущего дз (задание учебное, после выхода из программы
 управлением счетом в главной программе сумму и историю покупок можно не запоминать);
- смена рабочей директории (*необязательный пункт)
усложненное задание пользователь вводит полный /home/user/... или относительный user/my/... путь.
 Меняем рабочую директорию на ту что ввели и работаем уже в ней;
- выход
выход из программы.
Так же можно добавить любой другой интересный или полезный функционал по своему желанию
После выполнения какого либо из пунктов снова возвращаемся в меню, пока пользователь не выберет выход
3. Выложите проект на github:
4. Можно сдать задание в виде pull request:
5. Посмотреть разбор дз по функциям, если требуется, то сделать работу надо ошибками.1. Создать новый проект ""Консольный файловый менеджер"
"""

while True:
    print('1. создать папку')
    print('2. удалить (папку/файл)')
    print('3. копировать (папку/файл)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню - ')
    if choice == '1':
        deposit = float(input('\nВведите сумму на сколько пополнить счет --> '))
        if deposit > 0:
            balans += deposit
        print(f'На Вашем счёте --> {balans} у.е.')
    elif choice == '2':
        purchase = float(input('\nВведите сумму покупки --> '))
        if purchase > 0:
            if balans >= purchase:
                balans -= purchase
                name_goods = input('Введите название покупки (наименование товара) --> ')
                goods.append(name_goods)
                cost.append(purchase)
            else:
                print('Недостаточно средств на счёте')
        print(f'На Вашем счёте --> {balans} у.е.')
    elif choice == '3':
        print('\nИстория покупок')
        for i in range(len(goods)):
            print(f'{goods[i]} --> {cost[i]}')
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
