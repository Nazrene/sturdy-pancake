from cli import create_book, create_member, borrow_book, list_books, list_members

def main():
    while True:
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. List Books")
        print("5. List Members")
        print("6. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            create_book()
        elif choice == "2":
            create_member()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            list_books()
        elif choice == "5":
            list_members()
        elif choice == "6":
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
