from schedule import Schedule

# PSS Class

class PSS:

    def __init__(self):
        pass

    def add_task(self, task):
        pass

    def remove_task(self, task):
        pass

    def edit_task(self, task):
        pass

    def write_schedule_to_file(self, file):
        f = open(file, "w")
        for x in schedule.list_of_tasks:
            f.write(x)
        f.close()

    def read_schedule_from_file(self, file):
        f = open(file, "r")
        for x in f:
            add_task(x)
            print(x)
        f.close()

    def view_one_day_schedule(self):
        pass

    def view_one_week_schedule(self):
        pass

    def view_one_month_schedule(self):
        pass

    def find_task(self, task):
        pass
