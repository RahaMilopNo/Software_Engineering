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
