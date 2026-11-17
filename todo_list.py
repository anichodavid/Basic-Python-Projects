def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print ("----To-Do-List") 
    print ("1. Add task")   
    print ("2. View tasks") 
    print ("3. Delete task") 
    print ("4. Clear all tasks") 
    print ("5. Exit")

def add_task (tasks):
    task = input ("Enter task: ").strip()
    if task == "":
        print ("Task cannot be empty")
        return
    tasks.append(task)
    save_tasks(task)
    print (f"Added: {task}")

def view_task (tasks):
    if not tasks:
        print ("No tasks yet.")
        return
    print ("\nYour tasks:")
    for i, task in enumerate (tasks, start=1):
        print (f"{i}. {task}")

def delete_task(tasks):
    view_task(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete"))
    except ValueError:
        print("Please enter a valid number")
        return

    if num < 1 or num > len(tasks):
        print ("Invalid task number")
        return
    
    removed = tasks.pop(num - 1)
    save_tasks(tasks)
    print ("Deleted: {removed}")





def clear_all_tasks(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    confirm = input("Are you sure? This deletes ALL tasks (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.")
        return

    tasks.clear()          
    save_tasks(tasks)      
    print("All tasks deleted.")



def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            clear_all_tasks(tasks)
        elif choice == "5":
            print ("Goodbye!")
            break
        else:
            print("Invalid Choice")
            

if __name__ == "__main__":
    main()   


       

