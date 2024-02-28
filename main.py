from services import *
from repositories import *

if __name__ == "__main__":
    main()
    get_connection()


while True:
    choose = input("Введите номер действия: ")

    if choose == "1":
        get_todo_list()

    elif choose == "2":
        add_todo_task()

    elif choose == "3":
        delete_todo_task()

    elif choose == "0":
        break