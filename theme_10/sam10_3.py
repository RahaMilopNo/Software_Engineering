def add_two(user_input):
    try:
        number = float(user_input)
        result = 2 + number
        print(f"Результат: {result}")
    except ValueError:  
        print("Неподходящий тип данных. Ожидалось число.")
    except TypeError: 
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    add_two(5)      
    add_two("10.5") 
    add_two("abc")  
    add_two([1, 2]) 
