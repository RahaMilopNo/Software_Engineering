class FunctionCallTracker:
    def __init__(self, func):
        self.func = func
        self.calls = {}  

    def __call__(self, *args, **kwargs):
        if self.func.__name__ in self.calls:
            print(f"Функция '{self.func.__name__}' уже была вызвана ранее.")
        else:
            print(f"Функция '{self.func.__name__}' вызывается впервые.")
        
        self.calls[self.func.__name__] = self.calls.get(self.func.__name__, 0) + 1
        
        return self.func(*args, **kwargs)
# Первая функция: сложение двух чисел
@FunctionCallTracker
def add(a, b):
    result = a + b
    print(f"Результат сложения: {result}")
    return result
# Вторая функция: умножение двух чисел
@FunctionCallTracker
def multiply(a, b):
    result = a * b
    print(f"Результат умножения: {result}")
    return result

if __name__ == '__main__':
    add(3, 5)       
    add(2, 4)       
    multiply(2, 3)   
    multiply(5, 6)  
