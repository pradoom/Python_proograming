#Load Task Function
import os
TASK_FILE_PATH = "task.txt"
def Load_task():
    tasks = []
    #Check File exists or not
    if(os.path.exists(TASK_FILE_PATH)):
        with open(TASK_FILE_PATH,"r",encoding="utf-8") as f:
            #Read line by line
            for line in f:
                #Strip will remove extra line and extra spaces and rsplit will find "||" string from right side and split them in 0 and 1 strig 
                text,status= line.strip().rsplit("||",1)
                tasks.append({"text":text,"done":status=="done"})
    return tasks


def save_task(tasks):

    if(os.path.exists(TASK_FILE_PATH)):
        with open(TASK_FILE_PATH,"w",encoding="utf-8") as f:
            for task in tasks:
                status = "done" if task["done"] else "not_done"
                f.write(f"{task['text']} || {status}\n")


def display_task(tasks):
    if not tasks:
        print("Empty task list!")
    else:
        for i, task in enumerate(tasks, 1):
            checkbox = "✅" if task.get("done", False) else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    print()


def manage_tasks():
    #Load task from file
    tasks=Load_task()

    while True:
        print("/n ********************Task manager************************")

        print("1. For ADD TASK")
        print("2. View Task")
        print("3. Mark Task as Done")
        print("4. Delete TAsk")
        print("5. EXIT")

        option = input("Enter the Option form (1 to 5)").strip()

        print()
        print()
        print()

        match option:
            
            case "1":
                task = input("Enter tha TASK: ").strip()
                if task:
                    tasks.append({"text":task,"done":False})
                    save_task(tasks)
                else:
                    print("Task is empty Entered!")
            case "2":
                display_task(tasks)
            case "3":
                display_task(tasks)
                done_task = int(input("Enter task number:"))

                if(1<=done_task<=len(tasks)):
                    tasks[done_task-1]["done"] = True
                    save_task(tasks)
                    print("----After Task update----")
                    display_task(tasks)
            case "4":
                display_task(tasks)
                del_task = int(input("Enter task number:2"))

                if(1<=done_task<=len(tasks)):
                    tasks.pop(del_task-1)
                    save_task(tasks)
                print("----Delete Task update----")
                display_task(tasks)
            case "5":
                print("Exiting task Manager")
                break
            case _:
                print("Please choose a valid option")

manage_tasks()
