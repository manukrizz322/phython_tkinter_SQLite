import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        create table if not exists employees(
        id Integer Primary Key,
        name text,
        age text,
        doj text,
        email text,
        gender text,
        contact text,
        address varchar(200)
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, doj, email, gender, contact, address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                         (name, age, doj, email, gender, contact, address))
        self.con.commit()

    # fetch all Data from DB
    def fetch(self):
        self.cur.execute("select * from employees")
        rows = self.cur.fetchall()
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from employees where id =?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, age, doj, email, gender, contact, address):
        self.cur.execute("update employees set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?",
                         (name, age, doj, email, gender, contact, address, id))
        self.con.commit()



