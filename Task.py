

import sys
import json
import os
from datetime import datetime

TASKS_FILE = "task.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        try :
            return json.load(f)
        except json.JSONDecodeError :
            return []
        
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description , status) :
    tasks = load_tasks()
    task_id = max([t["id"] for t in tasks], default=0) + 1
    now = datetime.now().isoformat()
    task = {
        "id": task_id,
        "description": description,
        "status": status,
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(task)
    
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def delete_task (id ) :
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t['id'] != id]
    if len (tasks) == len(new_tasks) :
        print(f"there is no id like that ({id})")
    else :
        save_tasks(new_tasks)
        print("Task deleted successfully ")

def find_task_by_id(tasks, id):
    for task in tasks:
        if task["id"] == id:
            return task
    return None

def update_task (id , description , status ) :
    tasks = load_tasks()
    task = find_task_by_id ( tasks , id)
    if task == None :
        print(f"incorrect ID -> {id}")
        return False
    new_tasks = [t for t in tasks if t['id'] != id]
    now = datetime.now().isoformat()
    new_task = {
        "id": id,
        "description": description,
        "status": status,
        "createdAt": task['createdAt'],
        "updatedAt": now
    }
    new_tasks.append(new_task)

    save_tasks(new_tasks)
    print(f"Task updated successfully (ID: {id})")

import argparse 


p = argparse.ArgumentParser(description="Task Tracker CLI")
subp = p.add_subparsers(dest="command")

# Add command
add = subp.add_parser("add")
add.add_argument("description", help="Description of the task")
add.add_argument("status" , help= "status of the task")
# Delete command
delete = subp.add_parser("delete")
delete.add_argument("task_id", type=int, help="ID of the task to delete")

# Update command
update = subp.add_parser("update")
update.add_argument("task_id", type=int)
update.add_argument("description")
update.add_argument("status" , help= "status of the task")

# Mark and list can follow the same pattern...
args = p.parse_args()
print(args)
if args.command == "add" :
    add_task(args.description ,args.status)


if args.command == "delete" :
    delete_task(args.task_id)

if args.command == "update" :    
    update_task(args.task_id , args.description , args.status )
    
# Implement update, delete, mark-in-progress, mark-done, and list similarly...     1       3 


