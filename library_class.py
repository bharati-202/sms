class Book:
    def __init__(self, book_name, writer_name, language, price):
        self.book_name = book_name
        self.writer_name = writer_name
        self.language = language
        self.price = price

    def display_info(self):
        return f"Book Name: {self.book_name}, Writer Name: {self.writer_name}, Language: {self.language}, Price: {self.price}"

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book_name, writer_name, language, price):
        new_book = Book(book_name, writer_name, language, price)
        self.book_list.append(new_book)

    def show_books(self):
        if not self.book_list:
            print("No books in the library yet!")
        else:
            for book in self.book_list:
                print(book.display_info())

    def update_book(self, book_name, new_book_name=None, new_writer_name=None, new_language=None, new_price=None):
        for book in self.book_list:
            if book.book_name == book_name:
                if new_book_name:
                    book.book_name = new_book_name
                if new_writer_name:
                    book.writer_name = new_writer_name
                if new_language:
                    book.language = new_language
                if new_price:
                    book.price = new_price
                print(f"{book_name} updated successfully!")
                return
        print(f"Book named {book_name} not found!")

    def delete_book(self, book_name):
        for book in self.book_list:
            if book.book_name == book_name:
                self.book_list.remove(book)
                print(f"{book_name} deleted successfully!")
                return
        print(f"Book named {book_name} not found!")

def menu():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add a Book")
        print("2. Show Books")
        print("3. Update a Book")
        print("4. Delete a Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            book_name = input("Enter Book Name: ")
            writer_name = input("Enter Writer Name: ")
            language = input("Enter Language: ")
            price = float(input("Enter Price: "))
            library.add_book(book_name, writer_name, language, price)
        elif choice == '2':
            library.show_books()
        elif choice == '3':
            book_name = input("Enter Book Name to Update: ")
            new_book_name = input("Enter New Book Name (press Enter to skip): ")
            new_writer_name = input("Enter New Writer Name (press Enter to skip): ")
            new_language = input("Enter New Language (press Enter to skip): ")
            new_price = input("Enter New Price (press Enter to skip): ")
            new_price = float(new_price) if new_price else None
            library.update_book(book_name, new_book_name, new_writer_name, new_language, new_price)
        elif choice == '4':
            book_name = input("Enter Book Name to Delete: ")
            library.delete_book(book_name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    menu()
