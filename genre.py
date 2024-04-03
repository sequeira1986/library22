class Genre:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.bio = description

    @classmethod
    def from_db(cls, value):
        return cls(value[0], value[1], value[2])

    @staticmethod
    def vloz_do_db(cursor):
        print("Vlozte nazov zanru: ")
        meno = input()
        print("Vlozte popis zanru: ")
        desc = input()
        cursor.execute("INSERT INTO genres (name, description) VALUES (%s, %s)", (meno, desc))

    @staticmethod
    def zobraz_zanre(cursor):
        print("-- Zoznam zanrov --")
        cursor.execute("SELECT genre_id, name FROM genres")
        genres = cursor.fetchall()
        for genre in genres:
            print(f"ID: {genre[0]}, Name: {genre[1]}")