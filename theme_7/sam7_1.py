from collections import Counter

def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()

            word_count = len(words)
            most_common_word, most_common_count = Counter(words).most_common(1)[0]

            print(f"Количество слов: {word_count}")
            print(f"Самое часто встречающееся слово: '{most_common_word}' (встречается {most_common_count} раз)")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

count_words('sam7_1.txt')
