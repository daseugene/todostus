import sqlite3
from services import *


sqlite3.connect("todo.db")
con = sqlite3.connect("todo.db")
cursor = con.cursor()




def get_tasks():
    info = cursor.execute("SELECT * from tasks")

def insert_task(title, description):
    query = cursor.execute("INSERT INTO tasks VALUES"
                   f"('{title}', '{description}', false)")
    if query == True:
        return True
    row_please_row()



rows = cursor.fetchall()


def row_please_row():
    for row in rows:
        print(row)

