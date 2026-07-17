
from app import Library
from database_setup import initialize_database

def main():
    initialize_database()
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Loan Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. List Members")
        print("7. List Loans")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            publication_year = int(input("Enter publication year: "))
            library.add_book(title, author, isbn, publication_year)
        elif choice == "2":
            name = input("Enter member name: ")
            address = input("Enter member address: ")
            phone_number = input("Enter member phone number: ")
            library.add_member(name, address, phone_number)
        elif choice == "3":
            book_id = int(input("Enter book ID to loan: "))
            member_id = int(input("Enter member ID: "))
            library.loan_book(book_id, member_id)
        elif choice == "4":
            book_id = int(input("Enter book ID to return: "))
            library.return_book(book_id)
        elif choice == "5":
            print("\n--- All Books ---")
            for book in library.list_books():
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}, Year: {book[4]}, Status: {book[5]}")
        elif choice == "6":
            print("\n--- All Members ---")
            for member in library.list_members():
                print(f"ID: {member[0]}, Name: {member[1]}, Address: {member[2]}, Phone: {member[3]}")
        elif choice == "7":
            print("\n--- All Loans ---")
            for loan in library.list_loans():
                print(f"ID: {loan[0]}, Book ID: {loan[1]}, Member ID: {loan[2]}, Loan Date: {loan[3]}, Return Date: {loan[4]}")
        elif choice == "8":
            library.close()
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
