# Library as a dictionary
library = {}

def add_book():
    book_id = int(input("Enter Book ID: "))
    if book_id in library:
        print("Book ID is already exists!")
    else:
        book_name = input("Enter Book Name: ")
        writer_name = input("Enter Writer Name: ")
        price = int(input("Enter price: "))

        library[book_id] = {
            "Book Name" : book_name,
            "Writer Name" : writer_name,
            "Price" : price
        }
        view_book()
def view_book():
    if library:
        print("Books in Library: ")
        for book_id, data in library.items():
            print(f"ID: {book_id}, Book Name: {data['Book Name']}, Writer Name: {data['Writer Name']}, Price: {data['Price']}")

def edit_book():
    book_id = int(input("Enter Book ID to Update: "))
    if book_id in library:
        print("Current books Details!")
        print(f"Current Book ID: {library[book_id]['Book Name']}")
        print(f"Current Writer Name: {library[book_id]['Writer Name']}")
        print(f"Current Book price: {library[book_id]['Price']}")

        new_book_name = input("Enter new Book Name: ")
        new_writer_name = input("Enter new Writer Name: ")
        new_price = input("Enter new Price: ")

        if new_book_name:
            library[book_id]['Book Name'] = new_book_name
        if new_writer_name:
            library[book_id]['Writer Name'] = new_writer_name
        if new_price:
            library[book_id]['Price'] = new_price
        print("Book details updated successfully!")
        view_book()
    else:
        print("Book ID not found!")

def search_book():
    search_item = input("Enter Book Name or Writer Name: ").lower()
    found_books = []
    for book_id, details in library.items():
        if search_item in details['Book Name'].lower() or search_item in details['Writer Name'].lower():
            found_books.append((book_id, details))
    if found_books:
        print("Search Results: ")
        for book_id, details in found_books:
            print(f"Book ID: {book_id}, Book Name: {details['Book Name']}, Writer Name: {details['Writer Name']}, Price: {details['Price']}")
    else:
        print("No books found")


def delete_book():
    book_id = int(input("Enter Book ID to delete: "))
    if book_id in library:
        del library[book_id]
        print("Book deleted successfully!")
    else:
        print("Book ID not found!")
    view_book()

while True:
    print("Library menu: ")
    print("1: Add book")
    print("2: View books")
    print("3: Edit book")
    print("4: Search book")
    print("5: Delete book")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_book()
    elif choice == "3":
        edit_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        delete_book()
        break
    else:
        print("Invalid choice!")

