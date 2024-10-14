# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #4 выполнил(а):
- Куликов Максим Александрович
- ИВТ-22-1

| Задание    | Лаб_раб | Сам_раб |
|------------|---------| ------ |
| Задание 1  | +       | + |
| Задание 2  | +       | + |
| Задание 3  | +       | + |
| Задание 4  | +       | + |
| Задание 5  | +       | + |
| Задание 6  | +       |  |
| Задание 7  | +       |  |
| Задание 8  | +      |  |
| Задание 9  | +      |  |
| Задание 10 | +       |  |


знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа 7
## Задание №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.
### ![Результат]()
## Вывод
Создал файл input.txt и записал текст.

## Задание №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().
```python
f = open('input.txt', 'r')
print(f.readline())
f.close
```
### ![Результат]()
## Вывод
Написал код, который выводит первую строку с помощью open/close.

## Задание №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().
```python
f = open('input.txt', 'r')
print(f.readlines())
f.close
```
### ![Результат]()
## Вывод
Написал код, который выводит все строки в массиве.

## Задание №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().
```python
with open('input.txt') as f:
    print(f.readlines())
```
### ![Результат]()
## Вывод
Написал программу, который выводит все строки в массиве, с помощью конструкции with open().

## Задание №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().
```python
with open('input.txt') as f:
    for line in f:
        print(line)
```
### ![Результат]()
## Вывод
Написал программу, которая выводит каждую строку отдельно с помощью конструкции with open().

## Задание №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.
```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```
### ![Результат]()
## Вывод
Написал программу, которая добавляет новую строку в файл input.txt.

## Задание №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.
```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```
### ![Результат]()
## Вывод
Добавил в файл слова, one, two, three c помощью write().

## Задание №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит: ')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)

print_docs('C:/Users/rahat/Desktop/php')
```
### ![Результат]()
## Вывод
Написал программу, которая выводит в терминал все содержимое из директории с помощью функции print_docs(directory).

## Задание №9
### Документ «input.txt» содержит следующий текст:
### Приветствие
### Спасибо
### Извините
### Пожалуйста
### До свидания
### Ты готов?
### Как дела?
### С днем рождения!
### Удача!
### Я тебя люблю.
### Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных
```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words
    
print(longest_words('input.txt'))
```
### ![Результат]()
## Вывод
Написал программу, которая выводит максимально длинное слово из текста.

## Задание №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
### № - номер по порядку (от 1 до 300);
### Секунда – текущая секунда на вашем ПК;
### Микросекунда – текущая миллисекунда на часах.
### Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
### ![Результат]()
## Вывод
Написал программу, которая создает в csv файле столбцы с номером, секундой и микросекундой с остановкой скрипта 0.01 сек.


## Самостоятельная работа 7
## Задание №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово.
```python
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
```
### ![Результат]()
## Вывод
В этом задании я написал программу на Python, которая считает количество слов в текстовом файле и определяет самое часто встречающееся слово. Я использовал библиотеку collections.Counter для вычисления частоты слов.

## Задание №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль.
```python
import json
import os

EXPENSES_FILE = 'expenses.json'

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w', encoding='utf-8') as file:
        json.dump(expenses, file, ensure_ascii=False, indent=4)

def add_expense(expenses):
    date = input("Введите дату (YYYY-MM-DD): ")
    amount = float(input("Введите сумму расхода: "))
    category = input("Введите категорию расхода: ")
    description = input("Введите описание расхода: ")

    expense = {
        'date': date,
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Расход добавлен!")

def view_expenses(expenses):
    if not expenses:
        print("Нет записанных расходов.")
        return

    print("\nСписок расходов:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Дата: {expense['date']}, Сумма: {expense['amount']}, "
              f"Категория: {expense['category']}, Описание: {expense['description']}")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n1. Добавить расход")
        print("2. Показать расходы")
        print("3. Выход")
        
        choice = input("Выберите действие (1, 2 или 3): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == '__main__':
    main()
```
### ![Результат]()
## Вывод
В этом задании я написал программу для учета расходов, позволяющую добавлять, сохранять и просматривать данные. Я использовал библиотеку json для хранения информации в файл и реализовал простой интерфейс для управления расходами через консоль.

## Задание №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
### Текст в файле:
### Beautiful is better than ugly.
### Explicit is better than implicit.
### Simple is better than complex.
### Complex is better than complicated.
### Ожидаемый результат:
### Input file contains:
### 108 letters
### 20 words
### 4 lines
```python
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
```
### ![Результат]()
## Вывод
В этом задании я написал программу для подсчета количества букв, слов и строк в файле с текстом на латинице. Я использовал методы для подсчета символов, разделения слов и подсчета строк, чтобы вывести статистику по содержимому файла.

## Задание №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
### Запрещенные слова:
### hello email python the exam wor is
### Предложение для проверки:
### Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!
### Ожидаемый результат:
### *****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!
```python
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
```
### ![Результат]()
## Вывод
В этом задании я написал программу для замены запрещенных слов на звездочки в предложении, независимо от регистра и их местоположения в тексте. Я использовал регулярные выражения для поиска и замены запрещенных слов, загруженных из файла, и обеспечил точную замену даже в случае частичного совпадения.

## Задание №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
### Создайте текстовый файл input.txt, содержащий произвольный текст. Напишите программу, которая:Считывает текст из файла. Подсчитывает количество вхождений каждого слова (независимо от регистра). Сохраняет результаты в файл output.txt в формате: слово: количество.
```python
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
```
### ![Результат]()
## Вывод
В этом задании я написал программу, которая считывает текст из файла, подсчитывает количество вхождений каждого слова без учета регистра и сохраняет результат в файл. Я использовал библиотеку collections.Counter для подсчета и регулярные выражения для обработки текста.

## Общие выводы по теме
В заданиях я научился работать с текстовыми файлами, подсчитывать слова и символы, обрабатывать текст с помощью регулярных выражений, заменять запрещенные слова, а также сохранять результаты в новые файлы. Использование встроенных библиотек Python, таких как collections.Counter и re, упростило выполнение задач по анализу и обработке текста.
