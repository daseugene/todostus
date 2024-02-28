from repositories import *
def main():
    print("""
    1. Список задач
    2. Добавить задачу
    3. Удалить задачу
    """)




def connection():
    ...

def get_todo_list():
    ...

def add_todo_task():
    title, description = input("Заголовок: "), input("Описание: ")
    q = insert_task(title, description)
    if q == True:
        print("Задача создана")
    else:
        print("Что-то пошло не так")



def delete_todo_task():
    ...