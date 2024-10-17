class ValueOutOfRangeError(Exception):
    def __init__(self, message="Значение вышло за допустимые границы"):
        self.message = message
        super().__init__(self.message)

# Первая функция: проверка числа
def check_number(number, min_value, max_value):
    if number < min_value or number > max_value:
        raise ValueOutOfRangeError(f"Число {number} вне допустимого диапазона ({min_value}, {max_value})")
    else:
        print(f"Число {number} в допустимых пределах.")

# Вторая функция: проверка длины строки
def check_string(string, max_length):
    if len(string) > max_length:
        raise ValueOutOfRangeError(f"Длина строки превышает {max_length} символов")
    else:
        print(f"Длина строки в пределах {max_length} символов.")

if __name__ == '__main__':
    try:
        check_number(10, 1, 5)  
    except ValueOutOfRangeError as e:
        print(e)

    try:
        check_number(3, 1, 5)   
    except ValueOutOfRangeError as e:
        print(e)

    try:
        check_string("Привет", 3) 
    except ValueOutOfRangeError as e:
        print(e)

    try:
        check_string("Привет", 10) 
    except ValueOutOfRangeError as e:
        print(e)
