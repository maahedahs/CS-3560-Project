
# CS 3560 Project
# Group Members: Yennhi Dang, Maahedah Sadiq, Sam De Raimondo, Urjaa Ghimirey, Vraj Patel, Jacob Jung


from pss import PSS
from task import Task
from schedule import Schedule
import sys

if __name__ == '__main__':

    while 1:
        print("\nWelcome to the Personal Scheduling System.")
        print("1. Create a task")
        print("2. Delete a task")
        print("3. Edit a task")
        print("4. Write schedule to a file")
        print("5. Read schedule from a file")
        print("6. View a schedule")
        print("7. Exit")

        user_selection = int(input("\nEnter your selection: "))
        if user_selection == 1:
            choose_task_type = input("Enter 'T' for transient task, 'R' for recurring task, or 'A' for anti task: ")
            if choose_task_type == 'T' or choose_task_type == 't':
                task_name = input("Enter the task name you would like to create: ")
                task_type = input("Enter the type of task: Visit, Shopping, or Appointment for Transient task: ")
                task_start_date = input("Enter start date for the task: ")
                task_start_time = float(input("Enter start time for the task: "))
                task_duration = float(input("Enter duration for the task: "))

                ######
                #@TODO: pass all the task attributes to create task method 
                ######

            elif choose_task_type == 'R' or choose_task_type == 'r':
                task_name = input("Enter the task name you would like to create: ")
                task_type = input("Enter the type of task: Class, Study, Sleep, Exercise, Work, or Meal for Recurring task: ")
                task_start_date = input("Enter start date for the task: ")
                task_start_time = float(input("Enter start time for the task: "))
                task_duration = float(input("Enter duration for the task: "))
                task_end_date = input("Enter end date of the task: ")
                task_frequency = input("Enter task frequency as 1(Daily) or 7(Weeky): ")

                ######
                #@TODO: pass all the task attributes to create task method 
                ######

            elif choose_task_type == 'A' or choose_task_type == 'a':
                task_name = input("Enter the task name you would like to create for an Anti task: ")
                task_type = input("Enter the type of task: Cancellation for Anti task:  ")
                task_start_date = input("Enter start date for the anti task: ")
                task_start_time = float(input("Enter start time for the anti task: "))
                task_duration = float(input("Enter duration for the anti task: "))

                ######
                #@TODO: pass all the task attributes to create task method 
                ######
            else:
                print("\nError: Please choose your option between Transient task, Recurring task, or Anti task.")

        elif user_selection == 2:

            ######
            #@TODO: Get user input and pass to remove_task
            ######

            pass

        elif user_selection == 3:

            ######
            #@TODO: Get user input and pass to edit_task
            ######

            pass

        elif user_selection == 4:

            ######
            #@TODO: Ask for file name and pass to write_schedule_to_file
            ######

            pass

        elif user_selection == 5:

            ######
            #@TODO: Ask for file name and pass to read_schedule_to_file
            ######

            pass

        elif user_selection == 6:

            ######
            #@TODO: Get user input for a particular day, a week, or a month as well as the start date 
            ###### and call view_one_day_schedule, view_one_week_schedule, or view_one_month_schedule
            ######

            pass

        elif user_selection == 7:
            print("Thank you. Have a good day.")
            sys.exit(0)
        
        else:
            print("Error: please choose your option from 1 - 7: ")