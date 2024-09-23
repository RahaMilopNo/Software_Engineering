num = input("Введите число: ")
if num.isdigit() and 0 <= int(num) <= 10:
    num = int(num)
    print("Диапазон: 0-3" if num <= 3 else "Диапазон: 3-6" if num <= 6 else "Диапазон: 6-10")
else:
    print("Неверный ввод! Число должно быть от 0 до 10.")
