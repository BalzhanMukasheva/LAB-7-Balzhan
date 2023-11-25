# Напишите функцию для подсчета символов верхнего регистра в текстовом файле

def not_starting_with_D(file_name):
    try:
        # Открываем файл в режиме чтения с использованием 'with' для правильного закрытия
        with open(file_name, 'r') as file:
            # Считываем все строки файла и сохраняем их в переменную lines
            lines = file.readlines()

            # Используем генераторное выражение для подсчета строк, которые не начинаются с 'D'
            count = sum(1 for line in lines if not line.strip().startswith('D'))
            #strip() удаляет пробелы и символы новой строки с начала и конца строки
            # startswith('D') возвращает True, если строка начинается с 'D', или False

            # Выводим результат подсчета
            print(f"Вывод: {count}")

    except FileNotFoundError:
        # Обрабатываем случай, когда файл не найден
        print(f"Файл {file_name} не найден.")


# Вызываем функцию, передавая ей имя файла
not_starting_with_D("text1.txt")