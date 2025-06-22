import numpy as np
import pandas as pd
import sys

from datetime import datetime

class Task:
    def __init__(self, title, due_date, completion_status):
        self.title = title
        self.due_date = due_date
        self.completion_status = completion_status

Enter_user_name = input("enter a name : ").capitalize()
if not Enter_user_name:
    print("❌ name is empty or invalid input, kindly enter only letters only")
    sys.exit
    
Any_task = str(input("enter a task: ")).strip().lower()
if not Any_task:
    print("❌ Task is empty or incorrect input by user")
    sys.exit

Estimate_time = input("Estimated date (DD/MM/YY): ").strip()
if not Estimate_time:
    print("❌ Time is empty or incorrect input by user")
    sys.exit


try:
    due_date = datetime.strptime(Estimate_time, "%d/%m/%y")

    print("\nTask added (Kindly check your entered name, task and due date)")
    sys.exit
    print(f"user_name : {Enter_user_name}")
    print(f"task : {Any_task}")
    print(f"due date : {due_date.strftime('%d/%B/%Y')}")
    
except ValueError:
    print("Invalid date format: Please enter date in DD/MM/YY Format")
    

print("\nTask status (if Task had been completed enter completed otherwise, enter imcompleted)\n")

Task_status = input("enter status: ").strip().lower()

if Task_status == "completed":
    print("Task completed ✅")
if not Task_status:
    print("Task not completed or invalid input by user")
    sys.exit
elif Task_status != "completed":
    print("incomplete ❌, Task not completed or invalid input by user")
