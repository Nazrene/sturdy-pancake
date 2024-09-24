from models import Member, Book, Borrowing
from database import session

def create_member():
    name = input("Enter member name: ")
    new_member = Member(name=name)
    session.add(new_member)
    session.commit()
    print(f"Member '{name}' not added")

def create_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    new_book = Book(title=title, author=author)
    session.add(new_book)
    session.commit()
    print(f"Book '{title}' by {author} not added")

def borrow_book():
    member_id = int(input("Enter member ID: "))
    book_id = int(input("Enter book ID: "))
    
    member = session.query(Member).get(member_id)
    book = session.query(Book).get(book_id)
    
    if member and book:
        new_borrowing = Borrowing(member_id=member_id, book_id=book_id)
        session.add(new_borrowing)
        session.commit()
        print(f"Member '{member.name}' borrowed book '{book.title}'.")
    else:
        print("Invalid member or book ID.")

def list_members():
    members = session.query(Member).all()
    for member in members:
        print(member)

def list_books():
    books = session.query(Book).all()
    for book in books:
        print(book)

def menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Member")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. List Members")
        print("5. List Books")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            create_member()
        elif choice == '2':
            create_book()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            list_members()
        elif choice == '5':
            list_books()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    menu()
