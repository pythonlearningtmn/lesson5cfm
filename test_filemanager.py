"""
Создать модуль test_filemanager.py для тестирования функций консольного файлового менеджера.
В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше.
Это могут быть функции консольного файлового менеджера, а так же программы мой счет и программы викторина
(Дополнительно*) так же попробовать написать тесты для ""грязных"" функций, например копирования файла/папки, ...

Функции, используемые в вышеперечисленных программах:
print()
input()
os.listdir()        v
os.mkdir()          v
os.rmdir()          v
os.chdir()          v
os.remove()
os.getcwd()         v
os.uname()
os.path.isdir()
os.path.isfile()
shutil.copytree()
shutil.copyfile()
list()              v
victory()
bank_acc()
get_person_and_question()
get_random_person()            v

"""

import os
from my_functions import get_random_person

def test_mkdir_rmdir():
    """
    Тестируем две функции одновременно: mkdir() и rmdir()
    Будем создавать новый каталог "new_catalog", а затем его удалим.
    Каждый раз будем проверять наличие/отсутствие нового каталога
    :return:
    """
    # Проверяем отсутствие каталога "new_catalog"
    assert 'new_catalog' not in os.listdir()
    # Создаем новый каталог
    os.mkdir('new_catalog')
    # Проверяем наличие каталога на диске
    assert 'new_catalog' in os.listdir()
    # Удаляем каталог "new_catalog"
    os.rmdir('new_catalog')
    # Проверяем отсутствие каталога "new_catalog"
    assert 'new_catalog' not in os.listdir()

def test_chdir():
    """
    Тестируем функцию chdir() (и ещё раз протестируем mkdir() и rmdir())
    Сначала проверим отсутствие каталога "new_catalog".
    Затем создадим новый каталог "new_catalog".
    Проверим наличие нового каталога.
    Затем сменим рабочий каталог на "new_catalog".
    Проверим текущий рабочий каталог.
    Вернёмся назад в вышестоящий каталог и удалим "new_catalog"
    :return:
    """
    # Проверяем отсутствие каталога "new_catalog"
    assert 'new_catalog' not in os.listdir()
    # Создаем новый каталог
    os.mkdir('new_catalog')
    ls_dir = os.getcwd()            # Запоминаем имя текущего каталога
    ls = os.getcwd().split('/')
    ls.append('new_catalog')
    lsnew = "/".join(ls)            # формируем имя нового каталога для проверки
    # Проверяем наличие каталога на диске
    assert 'new_catalog' in os.listdir()
    # Сменим рабочий каталог на "new_catalog"
    os.chdir('new_catalog')
    # Проверяем текущий рабочий каталог
    assert lsnew == os.getcwd()
    # Возвращаемся в вышестоящий каталог
    os.chdir('..')
    # Проверяем текущий рабочий каталог (который был до смены каталога)
    assert ls_dir == os.getcwd()
    # Удаляем каталог "new_catalog"
    os.rmdir('new_catalog')
    # Проверяем отсутствие каталога "new_catalog"
    assert 'new_catalog' not in os.listdir()

def test_get_random_person():
    # кол-во возвращаемых элементов кортежа
    famous_people = {'Александр Сергеевич Пушкин': '06.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                     'Сергей Александрович Есенин': '03.10.1895', 'Владимир Семенович Высоцкий': '25.01.1938',
                     'Виктор Робертович Цой': '21.06.1962', 'Константин Эдуардович Циолковский': '17.09.1857',
                     'Сергей Павлович Королев': '12.01.1907', 'Валентин Петрович Глушко': '20.08.1908',
                     'Андрей Николаевич Туполев': '29.10.1888', 'Юрий Алексеевич Гагарин': '09.03.1934'}
    assert len(list(get_random_person())) == 2
    # вернулось то что есть в исходом словаре
    assert list(get_random_person())[0] in famous_people.keys()
    assert list(get_random_person())[1] in famous_people.values()
