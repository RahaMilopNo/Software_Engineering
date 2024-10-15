class Shape:  # Определение базового класса Shape
    def area(self):  # Метод, который должен быть переопределен в дочерних классах
        pass  # Пустая реализация метода

class Rectangle(Shape):  # Класс Rectangle, наследующий от Shape
    def __init__(self, width, height):  # Конструктор, принимающий ширину и высоту
        self.width = width  # Инициализация атрибута width 
        self.height = height  # Инициализация атрибута height

    def area(self):  # Переопределение метода area для расчета площади прямоугольника
        return self.width * self.height  # Возвращает произведение ширины и высоты

class Circle(Shape):  # Класс Circle, наследующий от Shape
    def __init__(self, radius):  # Конструктор, принимающий радиус круга
        self.radius = radius  # Инициализация атрибута radius 

    def area(self):  # Переопределение метода area для расчета площади круга
        return 3.14 * self.radius * self.radius  # Возвращает площадь круга 
    
# Создание объектов классов Rectangle и Circle
rect = Rectangle(5, 10)  # Прямоугольник 
circle = Circle(7)  # Круг 

print(f"Area of the rectangle: {rect.area()}")  # Вывод прямоугольника
print(f"Area of the circle: {circle.area()}")  # Вывод круга
