def count_uppercase_characters(file_name):
    try:
        # Открываем файл в режиме чтения с использованием 'with' для правильного закрытия
        with open(file_name, 'r') as file:
            content = file.read()
            #считывает все содержимое файла в виде строки. Полученная строка сохраняется в переменной content.
            uppercase_count = sum(1 for char in content if char.isupper())
            #Условие проверяет, является ли текущий символ прописной буквой
            # количество прописных букв в строке
            return uppercase_count

    except FileNotFoundError:
        # Handle the case when the file is not found
        print(f"File {file_name} not found.")
        return None

# Example usage:
file_name = "example.txt"
uppercase_count = count_uppercase_characters(file_name)

# Проверяем, был ли найден файл, и выводим результат
if uppercase_count is not None:
    print(f"Number of uppercase characters in the file: {uppercase_count}")