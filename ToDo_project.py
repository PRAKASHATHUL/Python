tasks={

}
id=1

def AddTask(task):
    global tasks
    global id
    tasks[id]={"tasks":task,"status":False}
    id+=1

def UpdateTask(task_id):
    global tasks
    my_task=tasks.get(task_id,"Tasks not found")
    try:
        my_task['status']=not my_task['status']
        print("Task updated successfully")
    except Exception as e:
        print(e)
        print("Failed to updated task")


def RemoveTask(id):
    pass

def ShowTask():
    print("Tasks")
    for k in tasks:
        print(f"{k} {tasks[k]['tasks']} - ","Done" if tasks[k]['status'] else "Incomplete")

while True:
    print("ToDo Tasks")
    print("1.Add Task\n2.Update Task\n3.Remove Task\n4.Show Task")
    choice=int(input("Enter your choice : "))
    match choice:
        case 1:
            task_count=int(input("How many task do you wish to enter : "))
            for k in range(task_count):
                task=input("Enter the task : ")
                AddTask(task)
        case 2:
            task_id=int(input("Enter the task id : "))
            UpdateTask(task_id)
        case 3:
            task_id = int(input("Enter the task id : "))
            RemoveTask(task_id)
        case 4:
            ShowTask()
        case __:
            print("Please enter valid choice")