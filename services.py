import time

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
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS tasktable(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, done BOOL)"
    )

def get_todo():
     sqlite3.connect("todo.db")
     con = sqlite3.connect("todo.db")
     cursor = con.cursor()

     q = ("SELECT id, title from tasktable")
     cursor.execute(q)
     rows = cursor.fetchall()
     for row in rows:
         print(*row)
     con.close()
     task_detail()



def add_todo_task():
    sqlite3.connect("todo.db")
    title, description = input("Заголовок: "), input("Описание: ")
    cursor.execute("INSERT INTO tasktable (title, description)"
                   f"VAlUES ('{title}', '{description}');"
                   )
    con.commit()



def task_detail():
    num_task = input("Посмотреть детали задачи № ")
   # value = f"'{num_task}'"
    cursor.execute("SELECT title FROM tasktable WHERE id=?", (num_task,))
    for row in cursor.fetchall():
        print()
        print("Заголовок: ",*row)
    cursor.execute("SELECT description FROM tasktable WHERE id=?", (num_task,))
    for row in cursor.fetchall():
        print("Описание: ",*row)
    cursor.execute("SELECT done FROM tasktable WHERE id=?", (num_task,))
    for row in cursor.fetchall():
        print("Статус: ", *row)
        print()

    choose = input("Поменять статус задачи? (y/n) ")
    if choose == "Y" or choose == "y":
        change_task_status(num_task)
    elif choose == "N" or choose == "n":
        choose = input("Удалить задачу? (y/n )")
        if choose == "Y" or choose == "y":
            delete_todo_task(num_task)
        elif choose == "N" or choose == "n":
            print("Возвращаемся в главное меню...")
            time.sleep(5)
            main()

def change_task_status(num_task):
    status = input("""
    Выберите статус задачи:
    1. Done
    2. To Do
    """)
    if status == "1":
        q = "UPDATE tasktable SET done = true"
        cursor.execute(q)
        con.commit()
        print("Данные обновлены")
        cursor.execute("SELECT title FROM tasktable WHERE id=?", (num_task,))
        for row in cursor.fetchall():
            print()
            print("Заголовок: ", *row)
        cursor.execute("SELECT description FROM tasktable WHERE id=?", (num_task,))
        for row in cursor.fetchall():
            print("Описание: ", *row)
            print()
        cursor.execute("SELECT done FROM tasktable WHERE id=?", (num_task,))
        for row in cursor.fetchall():
            print("Статус: ", *row)
            print()
    elif status == "2":
        q = "UPDATE tasktable SET done = false"
        cursor.execute(q)
        con.commit()
        print("Данные обновлены")




def delete_todo_task(num_task):
    q = "DELETE FROM tasktable WHERE id = ?"
    cursor.execute(q, (num_task,))
    con.commit()
    if True:
        print("Запись удалена")


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