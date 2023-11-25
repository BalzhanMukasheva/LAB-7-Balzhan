# Напишите функцию, которая должна читать каждый символ текстового файла, а также подсчитывать и
# отображать вхождения символов A и B (включая небольшие случаи)


def count_a_b(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read().lower()  # проходимы по содержимому и конвертируем в нижний регистр
            # используем count , чтобы подсчитать кол-во букв
            count_a = content.count('a')
            count_b = content.count('b')

            print(f"a={count_a}, b={count_b}")
    except FileNotFoundError:
        print(f"File {file_name} not found.")


# вызываем функцию
count_a_b("text1.txt")