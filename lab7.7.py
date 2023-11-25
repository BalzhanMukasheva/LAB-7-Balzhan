# Напишите программу для подсчета частоты слов в файле

def word_frequency(file_name):
    try:
        with open(file_name, 'r') as file:
            # Считываем содержимое и преобразуем к нижнему регистру
            content = file.read().lower()
            words = content.split()  # Разбиваем содержимое на слова

            word_count = {}
            for word in words:
                # Проверяем, встречается ли слово уже в словаре
                if word in word_count:
                    word_count[word] += 1
                    #Если слово уже есть в словаре, то увеличиваем значение счетчика для этого слова на 1
                else:
                    word_count[word] = 1

            # Выводим частоту слов
            for word, count in word_count.items():
                print(f"'{word}': {count}")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")

# Вызываем функцию, передавая имя файла
word_frequency("text1.txt")