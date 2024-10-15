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
