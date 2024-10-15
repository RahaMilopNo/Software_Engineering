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
