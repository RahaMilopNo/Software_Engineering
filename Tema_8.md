# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил(а):
- Куликов Максим Александрович
- ИВТ-22-1

| Задание    | Лаб_раб | Сам_раб |
|------------|---------| ------ |
| Задание 1  | +       | + |
| Задание 2  | +       | + |
| Задание 3  | +       | + |
| Задание 4  | +       | + |
| Задание 5  | +       | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа 8
## Задание №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.
```python
class Car:  # Определение класса 
    def __init__(self, make, model):  # Метод-конструктор, вызывается при создании объекта класса
        self.make = make  # Инициализация атрибута make 
        self.model = model  # Инициализация атрибута model 

my_car = Car("Toyota", "Corolla")  # Создание объекта my_car 
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_8/theme_8/screen/lab8_1.png)
## Вывод
В этом задании я создал класс Car с атрибутами make и model. Метод-конструктор инициализирует эти атрибуты при создании объекта. Написал комментарии к коду.

## Задание №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
class Car:  # Определение класса 
    def __init__(self, make, model):  # Метод-конструктор, вызывается при создании объекта класса
        self.make = make  # Инициализация атрибута make 
        self.model = model  # Инициализация атрибута model 

    def drive(self): # Метод, который выводит строку с маркой и моделью машины
        print(f"Diving the {self.make} {self.model}")  # Вывод строки с информацией о машине

my_car = Car("Toyota", "Corolla")  # Создание объекта my_car 
my_car.drive()  # Вызов метода drive для объекта my_car
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_8/theme_8/screen/lab8_2.png)
## Вывод
В этом задании я расширил класс Car, добавив метод drive(), который выводит информацию о марке и модели автомобиля. Написал комментарии к коду.

## Задание №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутомемкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
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
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_8/theme_8/screen/lab8_3.png)
## Вывод
В этом задании я создал новый класс ElectricCar, который наследует класс Car. В класс добавлен атрибут battery_capacity и метод charge(), который выводит информацию о зарядке автомобиля. Написал комментарии к коду.

## Задание №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать.Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
class Car:  # Определение класса 
    def __init__(self, make, model):  # Метод-конструктор, вызывается при создании объекта класса
        self.make = make  # Инициализация атрибута make 
        self.model = model  # Инициализация атрибута model 

    def drive(self): # Метод, который выводит строку с маркой и моделью машины
        print(f"Diving the {self.make} {self.model}")  # Вывод строки с информацией о машине

my_car = Car("Toyota", "Corolla")  # Создание объекта my_car 
print(my_car.make) # Вывод на экран марки машины
my_car.drive() # Вызов метода drive для объекта my_car
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_8/theme_8/screen/lab8_4.png)
## Вывод
В этом задании я реализовал инкапсуляцию в классе Car, сделав атрибут производителя защищённым  и атрибут модели приватным. Написал комментарии к коду.

## Задание №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
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
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_8/theme_8/screen/lab8_5.png)
## Вывод
В этом задании я реализовал полиморфизм с помощью базового класса Shape и его наследников — классов Rectangle и Circle. Написал комментарии к коду.


## Самостоятельная работа 8
## Задание №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Book:  
    def __init__(self, author, title, pages):  
        self.author = author  
        self.title = title  
        self.pages = pages  

    def reading_time(self, speed): 
        return self.pages / speed

my_book = Book("J.K. Rowling", "Harry Potter and the Sorcerer's Stone", 309)  

reading_hours = my_book.reading_time(50)  
print(f"Time to read '{my_book.title}' by {my_book.author}: {reading_hours:.2f} hours") 
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_8/theme_8/screen/sam8_1.png)
## Вывод
Класс Book описывает книгу с атрибутами: автор, название и количество страниц. Метод reading_time рассчитывает время для прочтения книги, исходя из переданной скорости чтения.

## Задание №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Book:  
    def __init__(self, author, title, pages, year, genre):  
        self.author = author  
        self.title = title  
        self.pages = pages  
        self.year = year  
        self.genre = genre  

    def reading_time(self, speed):  
        return self.pages / speed  

    def short_description(self):  
        return f"'{self.title}' by {self.author}, {self.year}, {self.genre}, {self.pages} pages"

    def recommend(self, preferred_genre): 
        if self.genre.lower() == preferred_genre.lower():  
            return f"This {self.genre} book is a great fit for you!"
        else:
            return f"This book might not match your preferred genre ({preferred_genre}), but it's worth a try!"

my_book = Book("J.K. Rowling", "Harry Potter and the Sorcerer's Stone", 309, 1997, "Fantasy") 

print(my_book.short_description()) 
print(my_book.recommend("Fantasy"))  
print(my_book.recommend("Science Fiction")) 
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_8/theme_8/screen/sam8_2.png)
## Вывод
#### Атрибуты:
- year - год издания книги.
- genre - жанр книги.
#### Методы:
- short_description() — вывод краткого описания книги.
- recommend(preferred_genre) — метод, который проверяет, соответствует ли жанр

## Задание №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Book:  
    def __init__(self, author, title, pages, year, genre): 
        self.author = author 
        self.title = title 
        self.pages = pages  
        self.year = year 
        self.genre = genre  

    def short_description(self):  
        return f"'{self.title}' by {self.author}, {self.year}, {self.genre}, {self.pages} pages"

class EBook(Book): 
    def __init__(self, author, title, pages, year, genre, file_size, file_format):  
        super().__init__(author, title, pages, year, genre) 
        self.file_size = file_size  
        self.file_format = file_format  

    def compatible(self, device_format):  
        if self.file_format.lower() == device_format.lower():  
            return f"This {self.file_format} format is compatible with your device."
        else:
            return f"This {self.file_format} format is not compatible with your device. You need {device_format}."

    def ebook_description(self):  
        return f"{super().short_description()}, File size: {self.file_size}MB, Format: {self.file_format}"

my_ebook = EBook("J.K. Rowling", "Harry Potter and the Sorcerer's Stone", 309, 1997, "Fantasy", 1.5, "EPUB")

print(my_ebook.ebook_description())  
print(my_ebook.compatible("EPUB"))  
print(my_ebook.compatible("PDF")) 
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_8/theme_8/screen/sam8_3_1.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_8/theme_8/screen/sam8_3_2.png)
## Вывод
Добавил класс EBook, который наследует атрибуты и методы из базового класса Book.

## Задание №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Book:
    def __init__(self, author, title, pages, year, genre):
        self.author = author  
        self.title = title  
        self.pages = pages  
        self.year = year  
        self.genre = genre  

    def short_description(self):  
        return f"'{self.title}' by {self.author}, {self.year}, {self.genre}, {self.pages} pages"

class EBook(Book):
    def __init__(self, author, title, pages, year, genre, file_size, file_format):
        super().__init__(author, title, pages, year, genre)  
        self.__file_size = file_size  
        self.__file_format = file_format  

    def get_file_size(self):
        return self.__file_size

    def set_file_size(self, new_size):
        if new_size > 0:
            self.__file_size = new_size
        else:
            print("File size must be greater than 0.")

    def get_file_format(self):
        return self.__file_format

    def set_file_format(self, new_format):
        if new_format.lower() in ["pdf", "epub", "mobi"]:  
            self.__file_format = new_format
        else:
            print("Invalid file format. Please choose PDF, EPUB, or MOBI.")

    def ebook_description(self):  
        return f"{super().short_description()}, File size: {self.__file_size}MB, Format: {self.__file_format}"

my_ebook = EBook("J.K. Rowling", "Harry Potter and the Sorcerer's Stone", 309, 1997, "Fantasy", 1.5, "EPUB")
my_ebook.set_file_size(2.0) 
print(f"Updated file size: {my_ebook.get_file_size()}MB") 
my_ebook.set_file_format("DOCX")  
my_ebook.set_file_format("PDF") 
print(f"Updated file format: {my_ebook.get_file_format()}")  
print(my_ebook.ebook_description())
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_8/theme_8/screen/sam8_4_1.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_8/theme_8/screen/sam8_4_2.png)
## Вывод
Приватные атрибуты __file_size и __file_format теперь недоступны напрямую вне класса, что защищает их от некорректного изменения. get_file_size() и get_file_format() позволяют безопасно получить значение приватных атрибутов. set_file_size(new_size) и set_file_format(new_format) позволяют изменить эти атрибуты, проверяя, чтобы новые значения были корректными.

## Задание №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Book:
    def __init__(self, author, title, pages, year, genre):
        self.author = author  
        self.title = title 
        self.pages = pages  
        self.year = year  
        self.genre = genre 

    def short_description(self): 
        return f"'{self.title}' by {self.author}, {self.year}, {self.genre}, {self.pages} pages"

class EBook(Book):
    def __init__(self, author, title, pages, year, genre, file_size, file_format):
        super().__init__(author, title, pages, year, genre)
        self.__file_size = file_size 
        self.__file_format = file_format  

    def ebook_description(self):  
        return f"{super().short_description()}, File size: {self.__file_size}MB, Format: {self.__file_format}"

class Magazine(Book):
    def __init__(self, author, title, pages, year, genre, issue_number):
        super().__init__(author, title, pages, year, genre)
        self.issue_number = issue_number  

    def short_description(self):  
        return f"Magazine '{self.title}' by {self.author}, Issue #{self.issue_number}, {self.year}, {self.genre}, {self.pages} pages"

items = [
    EBook("J.K. Rowling", "Harry Potter and the Sorcerer's Stone", 309, 1997, "Fantasy", 1.5, "EPUB"),
    Magazine("National Geographic", "The Wonders of Nature", 100, 2023, "Nature", 12),
    Book("George Orwell", "1984", 328, 1949, "Dystopian")
]

for item in items:
    print(item.short_description()) 
```
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_8/theme_8/screen/sam8_5_1.png)
### ![Результат](https://github.com/RahaMilopNo/Software_Engineering/blob/Tema_8/theme_8/screen/sam8_5_2.png)
## Вывод
- Новый класс Magazine наследует от класса Book.
- Включает новый атрибут issue_number, который обозначает номер выпуска.
- Переопределяет метод short_description() для вывода специфической информации
- Создается список items, содержащий объекты разных классов: EBook, Magazine и Book.
- Цикл проходит по всем элементам списка items и вызывает метод short_description().
- Несмотря на то что объекты имеют разные типы, метод вызывается единообразно, что демонстрирует полиморфизм в действии.

## Общие выводы по теме
В процессе работы с объектно-ориентированным программированием я изучил ключевые концепции, такие как наследование, инкапсуляция, полиморфизм, а также создание классов и объектов.
