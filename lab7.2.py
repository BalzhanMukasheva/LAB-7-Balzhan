import random


def random_line_file(file_name):
    try:
        # Пытаемся открыть файл для чтения
        with open(file_name, 'r') as file:
            # Читаем все строки из файла в список
            lines = file.readlines()
            #вызывается для объекта файла file. читает все строки из файла и возвращает их в виде списка строк.
            # Каждый элемент списка представляет собой одну строку из файла.

            # Проверяем, не является ли файл пустым
            if lines:
                # Выбираем случайную строку из списка
                #ыбирает случайную строку из списка lines, и эта строка затем выводится на экран.
                random_line = random.choice(lines)
                # Выводим случайную строку
                print("Random Line: ", random_line, end='')
            else:
                # Выводим сообщение, если файл пуст
                print("The file is empty.")
    except FileNotFoundError:
        # Выводим сообщение, если файл не найден
        print(f"Файл {file_name} не найден.")


# Вызываем функцию, передавая ей имя файла "text1.txt"
random_line_file("text1.txt")