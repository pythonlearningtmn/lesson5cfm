import os
def test_write_read():
    """
    Тестируем две новые функции: f.write() и f.read()
    Будем создавать новый файл, записывать в него строку, а затем читать и сравнивать с оригиналом.
    :return:
    """
    # Проверяем наличие/отсутствие файла "new_file.txt"
    if os.path.exists('new_file.txt'):
        assert 'new_file.txt' in os.listdir()
    else:
        assert 'new_file.txt' not in os.listdir()
    # Создаем/перезаписываем новый файл и записываем в него строку
    with open('new_file.txt', 'w') as f:
        f.write('new_text')
    # Читаем файл и проверяем (сравниваем) его содержимое с оригиналом
    with open('new_file.txt', 'r') as f:
        assert f.read() == 'new_text'
