def analyze_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            letter_count = sum(c.isalpha() for line in lines for c in line)
            word_count = sum(len(line.split()) for line in lines)
            line_count = len(lines)

            print("Input file contains:")
            print(f"{letter_count} letters")
            print(f"{word_count} words")
            print(f"{line_count} lines")
    
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

analyze_text('input1.txt')
