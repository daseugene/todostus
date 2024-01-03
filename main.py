import repositories


while True:

    print("1. Get your tasks \n 2. Create new task \n")

    move = int(input("Choose an action(type a number): "))
    # title = input("Print a title of your task: ")
    if move == 1:
        return.get_tasks()
