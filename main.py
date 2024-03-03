from services import *

if __name__ == "__main__":
    create_table()
    main()

while True:
    choose = input("Введите номер действия: ")

    if choose == "1":
        get_todo()

    elif choose == "2":
        add_todo_task()

    elif choose == "3":
        delete_choosed_tasks()

    elif choose == "0":

        break

    elif choose == "del":
        delete_all()