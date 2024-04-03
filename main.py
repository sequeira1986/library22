import psycopg2
from author import Author
from book import Book
from genre import Genre

conn = psycopg2.connect(
    dbname='brgeicfqg8kyazonirom',
    user='ulwgoripw8ejfilgoi5u',
    password='yIus83C46Zx1VgDBZ5UjzY04BQrST3',
    host='brgeicfqg8kyazonirom-postgresql.services.clever-cloud.com',
    port=50013
)

cursor = conn.cursor()


def vypis_menu():
    print("1. Pridat autora")
    print("2. Pridat zaner")
    print("3. Pridat knihu")


def aplikacia():
    while True:
        vypis_menu()
        choice = input("Vasa moznost: ")
        if choice == "1":
            Author.vloz_do_db(cursor)
            conn.commit()
        elif choice == "2":
            Genre.vloz_do_db(cursor)
            conn.commit()
        elif choice == "3":
            Author.zobraz_autorov(cursor)
            authorID = input("ID Authora: ")
            Genre.zobraz_zanre(cursor)
            genreID = input("ID zanru: ")
            Book.vloz_do_db(cursor, authorID, genreID)
            conn.commit()
        else:
            print("Neplatny vstup")


aplikacia()
