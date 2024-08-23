# Opening Message
print("Welcome to Devin's To Do List App!")

# Menu that displays the users options
def menu():
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

# Function that adds a task
def add_task():
    print("Add a Task")
    user_task = input("What task would you like to add? ").lower()
    try:
        tasks.append(user_task)
    except ValueError:
        print("Sorry something went wrong. Exiting to menu, Try again.")
    except TypeError:
        print("Oops something went wrong. Exiting to menu, Try again.")
    else:
        return tasks

# Function that removes a task
def remove_task():
    print("Delete a Task")
    for i in tasks:
        print("- ", i)
    target_task = input("What task would you like to delete?")
    try:
        if target_task not in tasks:
            print("Sorry I don't see that task, Try again.")
        else:
            tasks.remove(target_task)
            print("Task has been removed")
    except ValueError:
        print("Sorry something went wrong. Exiting to menu, Try again.")
    except TypeError:
        print("Something went wrong. Exiting to menu, Try again.")
    else:
        return tasks

# Function that will mark the tasks with complete / incomplete
def mark_complete():
    completed_tasks = []
    incomplete_tasks = []

    default_progress = "(Incomplete)"
    updated_progress = "(Complete)"
    for i in tasks:
        incomplete_tasks.append(i)
        inc_str_formula = i + " " + default_progress
        print(inc_str_formula)
    print("Mark a task complete")

    updated_task = input("Which task would you like to mark complete?").lower()
    if updated_task not in tasks:
        print("Sorry I don't understand. Exiting to menu")
    else:
        completed_tasks.append(updated_task)
        incomplete_tasks.remove(updated_task)
        print("Completed Tasks:")
        for a in completed_tasks:
            print(a + " " + updated_progress)
        print("Incomplete Tasks:")
        for b in incomplete_tasks:
            print(b)

# Function that views all the tasks
def view_tasks():
    print("Tasks: ")
    for i in tasks:
        print("- ", i)
    return tasks


session_terminate = False
tasks = []

# Running the application
while session_terminate == False:
    try:
        menu()
        user_input = input("Please select an option (1-5): ").lower()
        if user_input == "1":
            add_task()
        elif user_input == "2":
            view_tasks()
        elif user_input == "3":
            mark_complete()
        elif user_input == "4":
            remove_task()
        elif user_input == "5":
            session_terminate == True
            quit()
        else:
            menu()
            input("Sorry I don't understand. Please select an option (1-5): ")
    except ValueError:
        print("Value Error, please make sure to input the correct value type. (String or Integer)")
    finally:
        print("Thank you for using Devin's To Do App")
