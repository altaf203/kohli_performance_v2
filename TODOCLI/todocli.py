import json
from datetime import date

emptyDoc = False
task_count=0

while True:
    with open("todoDB.json","r") as f:
        todoData = json.load(f)
    # f = open("todoDB.json", "r")
    # todoData = json.load(f)
    # print(todoData, type(todoData))

    currentDate = date.today()
    if len(todoData) == 0:
        emptyDoc = True
        username = input("\n Hi there welcome to HIT , Please enter ur name :")
        todoData["name"] = username
        todoData["date"] = str(currentDate)
        
        # print("hey {username}! i hope you have a good start ")
        print("\n create a task by writing <create task> or <add task>")
        cmd = input(">>")

       
        todoData["today"] = []

        if cmd == "create task" or cmd == "add task":
            task_description = input("\n enter ur task description ")
            schedule_time = input("\n enter schedule time for the task ")

            task = {
                "task_id": task_count,
                "description" : task_description,
                "schedule_time" : schedule_time,
                "status": "TBD"
               
            }

            todoData["today"].append(task)

            with open("todoDB.json", "w") as f:
                json.dump(todoData, f, indent=4)
                
    elif "today" in list(todoData.keys()):
        # first print the existing task
        tasks = todoData["today"]
        username = todoData["name"]
        currentDate = todoData["date"]
        print(f"Today is {date}")
        print(f"\n Hey {username}, here are the tasks for ur days \n")

        for task in tasks:
            print(f"task number {tasks.index(task)+1}")
            print("\n task description :", task["description"])
            print("\n schedule time: ", task["schedule_time"])

        print("\n ceate another task")
        cmd = input(">>")

        if cmd == "create task" or cmd == "add task":
            task_description = input("\n enter ur task description ")
            schedule_time = input("\n enter schedule time for the task ")

            task = {
                "task_id": "task_count",
                "description" : task_description,
                "schedule_time": schedule_time,
                "status": "TBD"
            }

            todoData["today"].append(task)
            with open("todoDB.json", "r+") as f:
                f.seek(0)
                json.dump(todoData, f, indent=4)

            print("task created successful")
            print("if you want to add more task, type add task / create task ")
            print("if you are done for now plz type done")
            continue
        
        if cmd == "done" or cmd == "exit":
            print("have a graet day !!")
            break




