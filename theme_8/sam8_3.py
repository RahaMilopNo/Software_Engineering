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
