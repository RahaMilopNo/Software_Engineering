class Car:  # Определение класса 
    def __init__(self, make, model):  # Метод-конструктор, вызывается при создании объекта класса
        self.make = make  # Инициализация атрибута make 
        self.model = model  # Инициализация атрибута model 

    def drive(self): # Метод, который выводит строку с маркой и моделью машины
        print(f"Diving the {self.make} {self.model}")  # Вывод строки с информацией о машине

my_car = Car("Toyota", "Corolla")  # Создание объекта my_car 
my_car.drive()  # Вызов метода drive для объекта my_car
