import re
from collections import Counter

def count_word(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text.lower())
            
            word_count = Counter(words)

        with open(output_file, 'w', encoding='utf-8') as file:
            for word, count in word_count.items():
                file.write(f"{word}: {count}\n")

        print(f"Частота слов сохранена в файл '{output_file}'.")

    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

count_word('input4.txt', 'output.txt')
