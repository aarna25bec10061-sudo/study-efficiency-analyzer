task_list = []
def add_task():
    task_name = input("Enter the name of the task: ")
    if task_name.strip() == "":
        print("invalid Task name cannot be empty")
    else:
        task_list.append(task_name)
        print("Task added successfully")
def showtasks():
    if len(task_list) == 0:
        print("No tasks to show")
    else:
        for index, task in enumerate(task_list):
            print(f"{index + 1}. {task}")