
# Viewer Class

from task import RecurringTask, AntiTask, TransientTask

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
        print("7. View a task")
        print("8. Exit")

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
	

    def get_task_name(self):
        task_name = input("Enter the name of the task: ")
        return task_name

    def display_recurring_attributes(self, recurring_task):
        print('Name:', recurring_task.name)
        print('Type:', recurring_task.type)
        print('Start date:', recurring_task.start_date)
        print('Start time:', recurring_task.start_time)
        print('Duration:', recurring_task.duration)
        print('End date:', recurring_task.end_date)
        print('Frewuency:', recurring_task.frequency)

    def display_task_attributes(self, task):
        print('Name:', task.name)
        print('Type:', task.type)
        print('Start date:', task.start_date)
        print('Start time:', task.start_time)
        print('Duration:', task.duration)
    
    def write_to_file(self):
        file_name = input("Enter the name of the file you would like to write a schedule to: ")
        return file_name

    def read_from_file(self):
        file_name = input("Enter the name of the file you would like to read a schedule from: ")
        return file_name

    def view_day_schedule(self):
        task_date = input("Enter the day of the schedule you want to see: ")
        return task_date

    def view_week_schedule(self):
        task_week_start = input("Enter the start date of the week: ")
        task_week_end = input("Enter the end date of the week: ")
        return task_week_start, task_week_end

    def view_month_schedule(self):
        task_month_start = input("Enter the start date of the month: ")
        task_month_end = input("Enter the end date of the month: ")
        return task_month_start, task_month_end
