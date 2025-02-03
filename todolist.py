def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Quit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f'Task "{task}" added.')

def remove_task(tasks):
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed.')
    else:
        print(f'Task "{task}" not found.')

def show_tasks(tasks):
    if tasks:
        print("\nCurrent Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
    else:
        print("\nNo tasks available.")

def to_do_list():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            show_tasks(tasks)
            remove_task(tasks)
        elif choice == '3':
            show_tasks(tasks)
        elif choice == '4':
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")

to_do_list()