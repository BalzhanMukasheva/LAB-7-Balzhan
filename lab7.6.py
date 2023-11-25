# Напишите функцию для подсчета слов «all» и «none», присутствующих в текстовом файле.
# [Обратите внимание, что слова «all» и «none» являются полными словами]

def count_all_and_none(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            # считываеv все содержимое файла в виде строки.
            words = content.split()  # Разделяем содержимое на слова
            count_all = words.count("all")
            #count_all содержит количество вхождений слова "all" в текстовом файле.
            count_none = words.count("none")
            print(f"Количество слов 'all': {count_all}")
            print(f"Количество слов 'none': {count_none}")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")

# Вызываем функцию
count_all_and_none("text1.txt")