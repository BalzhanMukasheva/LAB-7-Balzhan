def read_and_display_file(file_name):
    try:
        # Пытаемся открыть файл для чтения
        with open(file_name, 'r') as file:
            # Читаем файл построчно и выводим на экран
            for line in file:
                print(line, end='')
                #следующий вызов print будет продолжаться на той же строке.
    except FileNotFoundError:
        # Выводим сообщение, если файл не найден
        print(f"Файл {file_name} не найден.")

# Вызываем функцию, передавая ей имя файла "text1.txt"
read_and_display_file("text1.txt")