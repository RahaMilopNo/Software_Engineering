class Car:  # Определение класса 
    def __init__(self, make, model):  # Метод-конструктор, вызывается при создании объекта класса
        self.make = make  # Инициализация атрибута make 
        self.model = model  # Инициализация атрибута model 

    def drive(self): # Метод, который выводит строку с маркой и моделью машины
        print(f"Diving the {self.make} {self.model}")  # Вывод строки с информацией о машине

my_car = Car("Toyota", "Corolla")  # Создание объекта my_car 
my_car.drive()  # Вызов метода drive для объекта my_car

class ElectricCar(Car):  # Определение класса ElectricCar, который наследуется от класса Car
    def __init__(self, make, model, battery_capacity):  # Конструктор для класса ElectricCar
        super().__init__(make, model)  # Вызов конструктора родительского класса Car для инициализации make и model
        self.battery_capacity = battery_capacity  # Инициализация атрибута battery_capacity 

    def charge(self):  # Метод, который выводит информацию о зарядке
        print(f"Charging the {self.make} {self.model}, {self.battery_capacity} kWh")  # Вывод строки с маркой, моделью и емкостью аккумулятора

my_electric_car = ElectricCar("Tesla", "Model S", 75)  # Создание объекта my_electric_car 
my_electric_car.drive()  # Вызов унаследованного метода drive
my_electric_car.charge()  # Вызов метода charge
