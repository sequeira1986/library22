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
        cursor.execute("INSERT INTO books (title, author_id, genre_id, isbn) VALUES (%s, %s, %s, %s)", (title, author_id, genre_id, isbn))