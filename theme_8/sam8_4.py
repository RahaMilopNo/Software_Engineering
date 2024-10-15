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
