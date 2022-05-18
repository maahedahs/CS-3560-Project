
# Viewer Class

import sys
from task import Task
from anti_task import AntiTask
from recurring_task import RecurringTask
from transient_task import TransientTask

class Viewer:

    def __init__(self):
        pass

    def display_main_menu(self):
        print("\nWelcome to the Personal Scheduling System.")
        print("1. Create a task")
        print("2. Delete a task")
        print("3. Edit a task")
        print("4. Write schedule to a file")
        print("5. Read schedule from a file")
        print("6. View a schedule")
        print("7. Exit")

    def create_transient_task(self):
        task_name = input("Enter the task name you would like to create: ")
        task_type = input("Enter the type of task: Visit, Shopping, or Appointment for Transient task: ")
        task_start_date = input("Enter start date for the task: ")
        task_start_time = float(input("Enter start time for the task: "))
        task_duration = float(input("Enter duration for the task: "))
        new_task = TransientTask(task_name, task_type, task_start_date, task_start_time, task_duration)
        return new_task

    def create_recurring_task(self):
        task_name = input("Enter the task name you would like to create: ")
        task_type = input("Enter the type of task: Class, Study, Sleep, Exercise, Work, or Meal for Recurring task: ")
        task_start_date = input("Enter start date for the task: ")
        task_start_time = float(input("Enter start time for the task: "))
        task_duration = float(input("Enter duration for the task: "))
        task_end_date = input("Enter end date of the task: ")
        task_frequency = input("Enter task frequency as 1(Daily) or 7(Weeky): ")
        new_task = RecurringTask(task_name, task_type, task_start_date, task_start_time, task_duration, task_end_date, task_frequency)
        return new_task

    def create_anti_task(self):
        task_name = input("Enter the task name you would like to create for an Anti task: ")
        task_type = input("Enter the type of task: Cancellation for Anti task: ")
        task_start_date = input("Enter start date for the anti task: ")
        task_start_time = float(input("Enter start time for the anti task: "))
        task_duration = float(input("Enter duration for the anti task: "))
        new_task = AntiTask(task_name, task_type, task_start_date, task_start_time, task_duration)
        return new_task

    def remove_task(self):
        task_name = input("Enter the task name you would like to remove: ")
        return task_name