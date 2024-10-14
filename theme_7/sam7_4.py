import re

def load_forbidden_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            forbidden_words = file.read().strip().split()
        return set(forbidden_words)  
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return set()

def replace_forbidden_words(sentence, forbidden_words):
    def replacement(match):
        return '*' * len(match.group())

    pattern = r'(?i)\b(' + '|'.join(re.escape(word) for word in forbidden_words) + r')\b|(' + '|'.join(re.escape(word) + r'[^\w\s]*' for word in forbidden_words) + r')'
    
    modified_sentence = re.sub(pattern, replacement, sentence)
    return modified_sentence

def main():
    forbidden_words = load_forbidden_words('input3.txt')
    sentence = input("Введите предложение: ")

    modified_sentence = replace_forbidden_words(sentence, forbidden_words)

    print(modified_sentence)

if __name__ == '__main__':
    main()
