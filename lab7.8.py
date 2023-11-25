#Самое длинное слово
def find_longest_word(file_name):
    try:
        with open(file_name, 'r') as file:
            # Считываем содержимое файла
            content = file.read()

            # Разбиваем текст на слова
            words = content.split()

            # Инициализируем переменную для хранения самого длинного слова
            longest_word = ""

            # Перебираем слова и находим самое длинное
            for word in words:
                if len(word) > len(longest_word):
                    #Проверяем, длиннее ли текущее слово, чем самое длинное из ранее найденных.
                    longest_word = word
                    #Если текущее слово длиннее, обновляем переменную

            # Выводим результат
            print(f"Самое длинное слово: '{longest_word}'")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")

# Вызываем функцию, передавая имя файла
find_longest_word("text1.txt")