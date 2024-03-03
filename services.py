import time

from repositories import *
import sqlite3

rows = cursor.fetchall()

def main():
    print("""
    1. Список задач
    2. Создать задачу
    """)
    create_table()

def create_table():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS tasktable(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, done BOOL)"
    )

def get_todo():
     q = ("SELECT id, title from tasktable")
     cursor.execute(q)
     rows = cursor.fetchall()
     lst = rows
     # print("__________")
     # print(lst)
     # print("__________")
     if lst:
         for row in rows:
             print(*row)
         time.sleep(2)
         task_detail()

     else:
         print("""
                           Список задач пуст.
                           Создайте задачу для начала работы.
                           """)
         print()
         time.sleep(1.5)
         add_todo_task()




def add_todo_task():
    title, description = input("Заголовок: "), input("Описание: ")
    cursor.execute("INSERT INTO tasktable (title, description, done)"
                   f"VAlUES ('{title}', '{description}', false);"
                   )
    con.commit()
    time.sleep(1.5)
    print("""
    Задача успешно создана!
    
    Возвращаемся в главное меню...
    """)
    time.sleep(1.5)
    main()




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
    0. To Do
    """)
    print()
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

        time.sleep(1.5)
        print("Возвращаемся в главное меню...")
        time.sleep(1.5)
        main()
    elif status == "0":
        q = "UPDATE tasktable SET done = false"
        cursor.execute(q)
        con.commit()
        time.sleep(0.3)
        print("""
        Данные обновлены.
        Текущий статус 'To Do'(0)
        """)
        time.sleep(1.5)
        print("Возвращаемся в главное меню...")
        time.sleep(1.5)
        main()


def delete_choosed_tasks():
    q = "SELECT MAX(id) FROM tasktable"
    qq = int(q)
    lst = []
    for i in range(qq):
        lst.append(int(input()))
    q = "DELETE FROM tasktable WHERE id = ?"
    cursor.execute(q, (lst,))
    con.commit()



def delete_todo_task(num_task):
    q = "DELETE FROM tasktable WHERE id = ?"
    cursor.execute(q, (num_task,))
    con.commit()
    if True:
        print("Запись удалена")
        main()


def delete_all():
    q = ("DELETE FROM tasktable")
    cursor.execute(q)
    q = "DROP TABLE tasktable"
    cursor.execute(q)
    con.commit()
    print()
    print("ALL DATA HAS BEEN DELETED")
    print()
    main()
    con.close()
    sqlite3.connect("todo.db")