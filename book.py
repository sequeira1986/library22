class Book:
    def __init__(self, id, title, author_id, genre_id, isbn, publication_year, copies):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.publication_year = publication_year
        self.copies = copies

    @classmethod
    def from_db(cls, value):
        return cls(value[0], value[1], value[2])

    @staticmethod
    def vloz_do_db(cursor, author_id, genre_id):
        print("Vlozte nazov knihy ")
        title = input()
        print("Vlozte ISBN: ")
        isbn = input()
        cursor.execute("INSERT INTO books (title, author_id, genre_id, isbn) VALUES (%s, %s, %s, %s)",
                       (title, author_id, genre_id, isbn))

    @staticmethod
    def delete_book(cursor):
        print("Vlozte nazov knihy ")
        title = input()
        cursor.execute("DELETE FROM books WHERE title = %s", (title,))
        print("Kniha bola vymazana")

    @staticmethod
    def pocicaj_knihu(cursor, member_id, id):
        cursor.execute("SELEC copies FROM books WHERE id= %s", id)
        result = cursor.fetchone()[0]
        if result and result[0] > 0:
            # Book is available, update copies count and insert into loans table
            cursor.execute("UPDATE books SET copies = copies - 1 WHERE book_id = %s", id)
            cursor.execute("INSERT INTO loans (member_id, book_id) VALUES (%s, %s)", (member_id, id))
            print("Book borrowed successfully.")
        else:
            print("Book is not available for borrowing.")

    @staticmethod
    def return_book(cursor, member_id, id):
        # Update copies count and delete record from loans table
        cursor.execute("UPDATE books SET copies = copies + 1 WHERE book_id = %s", (id,))
        cursor.execute("DELETE FROM loans WHERE member_id = %s AND book_id = %s", (member_id, id))
        print("Book returned successfully.")

