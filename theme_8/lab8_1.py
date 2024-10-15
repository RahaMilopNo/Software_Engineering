class Car:  # Определение класса 
    def __init__(self, make, model):  # Метод-конструктор, вызывается при создании объекта класса
        self.make = make  # Инициализация атрибута make 
        self.model = model  # Инициализация атрибута model 

my_car = Car("Toyota", "Corolla")  # Создание объекта my_car 
