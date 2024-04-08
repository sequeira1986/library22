from turtle import title

import psycopg2
from loans import LoanManager

from author import Author
from book import Book
from genre import Genre
from members import Member

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
    print("4. vymazat knihu")
    print("5.pridaj clena")
    print("6.vymas clena")
    print("7. pocicat knihu")
    print("8. Vratit knihu")
    print("9. aktualne pocicane")
    print("10. pedhazajuce pocicky")


def aplikacia():
    while True:
        vypis_menu()
        choice = input("Vasa moznost: ")
        # vloz_do_dd is a method from the class Author
        # A cursor is a data access object that can be used to either iterate
        # over the set of rows in a table or insert new rows into a table.
        # Cursors have three forms: search, insert, and update.
        if choice == "1":
            Author.vloz_do_db(cursor)
            conn.commit()
        elif choice == "2":
            Genre.vloz_do_db(cursor)
            conn.commit()
        elif choice == "3":
            Author.zobraz_autorov(cursor)
            author_id = input("Vyberte ID autora: ")
            Genre.zobraz_zanre(cursor)
            genre_id = input("Vyberte ID žánru: ")
            Book.vloz_do_db(cursor, author_id, genre_id)
            conn.commit()

        elif choice == "4":
            Book.delete_book(cursor)
            conn.commit()
        elif choice == "5":
            first_name = input("Meno : ")
            last_name = input("Priezvisko :")
            email = input("email: ")
            Member.registracia_member(cursor, first_name, last_name, email)
            conn.commit()
        elif choice == "6":
            member_id = input("ID Člena: ")
            Member.delete_member(cursor, member_id)
            conn.commit()
        elif choice == "7":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            Book.pocicaj_knihu(cursor, member_id, book_id)
            conn.commit()
        elif choice == "8":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            Book.return_book(cursor, member_id, book_id)
            conn.commit()
        elif choice == "9":
            member_id = input("Member ID: ")
            current_loans = LoanManager.get_current_loans(cursor, member_id)
            if current_loans:
                print("Current loans:")
                for loan in current_loans:
                    print(loan)
            else:
                print("nie su pozicky")


        elif choice == "10":

            member_id = input("Member ID: ")

            past_loans = LoanManager.get_past_loans(cursor, member_id)

            if past_loans:

                print("Past loans:")

                for loan in past_loans:
                    print(loan)  # Modify this to display loan details as needed

            else:

                print("No past loans found.")

        else:

            print("Neplatný vstup")


aplikacia()
