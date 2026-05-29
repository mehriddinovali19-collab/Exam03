class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
book1 = Book("Atomic Habits", "James Clear", 2018)
book2 = Book("harry potter", "J.K Rowling", 2002)

print(book1.title, book1.author, book1.year)
print(book2.title, book2.author, book2.year)

