from repositories import *
import sqlite3

rows = cursor.fetchall()


def main():
    print("""
    1. Список задач
    2. Добавить задачу
    3. Удалить задачу
    """)
    create_table()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS tasktable(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, done BOOL)")

def get_todo():
     sqlite3.connect("todo.db")
     con = sqlite3.connect("todo.db")
     cursor = con.cursor()

     q = ("SELECT id, title from tasktable")
     cursor.execute(q)
     rows = cursor.fetchall()
     for row in rows:
         print(row)
     con.close()


def add_todo_task():
    sqlite3.connect("todo.db")
    title, description = input("Заголовок: "), input("Описание: ")
    cursor.execute("INSERT INTO tasktable (title, description)"
                   f"VAlUES ('{title}', '{description}');"
                   )
    con.commit()
    con.close()


def delete_todo_task():
    ...


def delete_all():
    sqlite3.connect("todo.db")
    con = sqlite3.connect("todo.db")
    cursor = con.cursor()
    q = ("DELETE FROM tasktable")
    cursor.execute(q)
    con.commit()
    print()
    print("ALL DATA HAS BEEN DELETED")
    print()
    con.close()