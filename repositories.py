import sqlite3


con = sqlite3.connect("todo.db")
cursor = con.cursor()


def create_table():
    cursor.execute("CREATE TABLE tasks(title, description, done)")



def get_tasks():
    return(cursor.execute("SELECT * from tasks"))

def insert_task(title, description):
    cursor.execute("INSERT INTO tasks VALUES"
                   f"('{title}', '{description}', false)")




rows = cursor.fetchall()

for row in rows:
    print(row)

