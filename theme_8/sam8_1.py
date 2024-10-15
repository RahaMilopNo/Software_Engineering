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
