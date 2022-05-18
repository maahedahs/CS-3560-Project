# CS 3560 Project
# Group Members: Yennhi Dang, Maahedah Sadiq, Sam De Raimondo, Urjaa Ghimirey, Vraj Patel, Jacob Jung


from pss import PSS
from task import Task
from schedule import Schedule
from viewer import Viewer
import sys

if __name__ == '__main__':
    viewer = Viewer()
    pss = PSS()

    while 1:
        viewer.display_main_menu()
        user_selection = int(input("\nEnter your selection: "))
        
        if user_selection == 1:
            choose_task_type = input("Enter 'T' for transient task, 'R' for recurring task, or 'A' for anti task: ")
            if choose_task_type == 'T' or choose_task_type == 't':
                new_task = viewer.create_transient_task()
                pss.add_task(new_task)    
            elif choose_task_type == 'R' or choose_task_type == 'r':
                new_task = viewer.create_recurring_task()
                pss.add_task(new_task)
            elif choose_task_type == 'A' or choose_task_type == 'a':
                new_task = viewer.create_anti_task()
                pss.add_task(new_task)
            else:
                print("\nError: Please choose your option between Transient task, Recurring task, or Anti task.")
        
        elif user_selection == 2:
            task_name = viewer.remove_task()
            task_to_remove = pss.find_task(task_name)
            pss.remove_task(task_to_remove)

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
