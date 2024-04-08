class Member:
    def __init__(self, member_id, first_name, last_name, email, ):
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    @classmethod
    def from_db(cls,value):
        return cls(value[0], value[1],value[2], value[3])

    @staticmethod
    def registracia_member(cursor, first_name, last_name, email):
        print("vlozte udaje")
        cursor.execute("INSERT INTO members (first_name, last_name,  email) VALUES (%s, %s, %s)", (first_name, last_name, email))
        print("Member bol vytvorene uzpecne.")

    @staticmethod
    def delete_member(cursor, member_id):
        cursor.execute("DELETE FROM members WHERE member_id = %s", (member_id,))
        print("Členstvo bol vymasane z databáze.")

    @staticmethod
    def display_current_loans(cursor, member_id):
        cursor.execute("SELECT b.title FROM loans l JOIN books b ON l.book_id = b.book_id WHERE l.member_id = %s", (member_id,))
        current_loans = cursor.fetchall()
        if current_loans:
            print("Current loans:")
            for loan in current_loans:
                print(loan[0])
        else:
            print("No current loans for this member.")
    @staticmethod
    def display_past_loans(cursor, member_id):
        cursor.execute("SELECT b.title FROM loans l JOIN books b ON l.book_id = b.book_id  WHERE l.member_id = %s AND "
                       "l.returned = TRUE", (member_id,))
        past_loans = cursor.fetchall()
        if past_loans:
            print("Past loans:")
            for loan in past_loans:
                print(loan[0])
        else:
            print("No past loans for this member.")




