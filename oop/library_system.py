class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_details(self) -> str:
        return f"Book: {self.title} by {self.author}"
    
    def __str__(self) -> str:
        return self.get_details()


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self) -> str:
        base_details = super().get_details()
        clean_base_details = base_details.replace("Book: ", "")
        return f"EBook: {clean_base_details}, File Size: {self.file_size}KB"
    
    def __str__(self) -> str:
        return self.get_details()
    
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
    
    def get_details(self) -> str:
        base_details = super().get_details()
        clean_base_details = base_details.replace("Book: ", "")
        return f"PrintBook: {clean_base_details}, Page Count:   {self.page_count} pages"

class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book: Book):
        if isinstance (book, Book):
            self.books.append(book)

        else:
            print(f"Cannot add non-Book object: {type(book)}")

    def list_books(self):
        if not self.book:
            print("Library does not have books")
            return
    
        for book in self.books:
            print(book)