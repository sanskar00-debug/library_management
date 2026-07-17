
import sqlite3
from datetime import datetime

class Library:
    def __init__(self, db_name='library.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def _execute_query(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def add_book(self, title, author, isbn, publication_year):
        query = "INSERT INTO books (title, author, isbn, publication_year) VALUES (?, ?, ?, ?)"
        if self._execute_query(query, (title, author, isbn, publication_year)):
            print(f"Book '{title}' added successfully.")

    def add_member(self, name, address, phone_number):
        query = "INSERT INTO members (name, address, phone_number) VALUES (?, ?, ?)"
        if self._execute_query(query, (name, address, phone_number)):
            print(f"Member '{name}' added successfully.")

    def loan_book(self, book_id, member_id):
        # Check if book is available
        self.cursor.execute("SELECT status FROM books WHERE id = ?", (book_id,))
        book_status = self.cursor.fetchone()

        if book_status and book_status[0] == 'available':
            loan_date = datetime.now().strftime("%Y-%m-%d")
            query = "INSERT INTO loans (book_id, member_id, loan_date) VALUES (?, ?, ?)"
            if self._execute_query(query, (book_id, member_id, loan_date)):
                self._execute_query("UPDATE books SET status = 'on loan' WHERE id = ?", (book_id,))
                print(f"Book {book_id} loaned to member {member_id} successfully.")
        else:
            print(f"Book {book_id} is not available for loan.")

    def return_book(self, book_id):
        # Check if book is on loan
        self.cursor.execute("SELECT id FROM loans WHERE book_id = ? AND return_date IS NULL", (book_id,))
        loan_id = self.cursor.fetchone()

        if loan_id:
            return_date = datetime.now().strftime("%Y-%m-%d")
            query = "UPDATE loans SET return_date = ? WHERE id = ?"
            if self._execute_query(query, (return_date, loan_id[0])):
                self._execute_query("UPDATE books SET status = 'available' WHERE id = ?", (book_id,))
                print(f"Book {book_id} returned successfully.")
        else:
            print(f"Book {book_id} was not on loan.")

    def list_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def list_members(self):
        self.cursor.execute("SELECT * FROM members")
        return self.cursor.fetchall()

    def list_loans(self):
        self.cursor.execute("SELECT * FROM loans")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    # Example Usage (for testing purposes)
    from database_setup import initialize_database
    initialize_database()

    library = Library()

    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 1925)
    library.add_book("1984", "George Orwell", "978-0451524935", 1949)
    library.add_member("Alice Smith", "123 Main St", "555-1234")
    library.add_member("Bob Johnson", "456 Oak Ave", "555-5678")

    print("\nBooks:")
    for book in library.list_books():
        print(book)

    print("\nMembers:")
    for member in library.list_members():
        print(member)

    library.loan_book(1, 1) # Alice loans The Great Gatsby
    library.loan_book(2, 1) # Alice loans 1984
    library.loan_book(1, 2) # Bob tries to loan The Great Gatsby (should fail)

    print("\nLoans:")
    for loan in library.list_loans():
        print(loan)

    library.return_book(1)

    print("\nBooks after return:")
    for book in library.list_books():
        print(book)

    print("\nLoans after return:")
    for loan in library.list_loans():
        print(loan)

    library.close()
