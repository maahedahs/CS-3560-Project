
# Schedule Class

from task import AntiTask, RecurringTask, TransientTask

class Schedule:

    def __init__(self):
        self.list_of_tasks = []

    def __init__(self, list_of_tasks):
        self.list_of_tasks = []
        for i in list_of_tasks:
            unique_name = self.check_task_name(i.name)
            valid_date = self.check_valid_date(i.start_date)
            task_overlap = self.check_for_overlapping_tasks(i)
            if unique_name == True and valid_date == True and task_overlap == True:
                self.list_of_tasks.append(i)
            else:
                print("Task not added to schedule:", i.name, unique_name, valid_date, task_overlap)

    def add_task_to_schedule(self, task):
        unique_name = self.check_task_name(task.name)
        valid_date = self.check_valid_date(task.start_date)
        task_overlap = self.check_for_overlapping_tasks(task)
        if unique_name == True and valid_date == True and task_overlap == True:
            self.list_of_tasks.append(task)
        else:
            print("Task not added to schedule:", task.name, unique_name, valid_date, task_overlap)
    
    def check_for_overlapping_tasks(self, task):
        start_time = task.start_time
        end_time = start_time + task.duration
        anti_task = isinstance(task, AntiTask)

        # check that an anti task overlaps with a recurring task
        if anti_task == True:
            for i in self.list_of_tasks:
                if not isinstance(i, RecurringTask):
                    continue
                check_start_time = i.start_time
                check_end_time = check_start_time + i.duration
                list_of_recurring_dates = self.get_list_of_recurring_dates(i)
                if task.start_date in list_of_recurring_dates and start_time == check_start_time and end_time == check_end_time:
                    i.list_of_anti_tasks.append(task)
                    return True
            return False

        # check that recurring and transient tasks do not overlap with any other tasks
        else:
            for i in self.list_of_tasks:
                if isinstance(i, RecurringTask):
                    list_of_recurring_dates = self.get_list_of_recurring_dates(i)
                    if task.start_date not in list_of_recurring_dates:
                        continue
                elif isinstance(i, TransientTask) and i.start_date != task.start_date:
                    continue
                check_start_time = i.start_time
                check_end_time = check_start_time + i.duration
                # if task starts in the middle of another task
                if start_time < check_end_time and start_time > check_start_time:
                    return False
                # if task ends in the middle of another task
                elif end_time < check_end_time and end_time > check_start_time:
                    return False
                # if task starts and ends at the same time as another task
                elif end_time == check_end_time and start_time == check_start_time:
                    return False
            return True

    def get_list_of_recurring_dates(self, task):
        list_of_dates = []
        next_date = task.start_date
        list_of_dates.append(task.start_date)
        months_31 = [1, 3, 5, 7, 8, 10, 12]
        months_30 = [4, 6, 9, 11]
        if task.frequency == 7:
            increment = 1
        elif task.frequency == 1:
            increment = 7

        while next_date != task.end_date:
            year = int(next_date[0:4])
            month = int(next_date[4:6])
            day = int(next_date[6:8])
            next_day = day + increment
            if month in months_31 and next_day > 31:
                month += 1
                next_day = next_day - 31
            elif month in months_30 and next_day > 30:
                month += 1
                next_day = next_day - 30
            elif month == 2 and year % 4 == 0 and day > 29:
                month += 1
                next_day = next_day - 29
            elif month == 2 and day > 28:
                month += 1
                next_day = next_day - 28
            if month > 12:
                year += 1
                month = 1

            str_year = str(year)
            if month < 10:
                str_month = '0' + str(month)
            else:
                str_month = str(month)
            if next_day < 10:
                str_day = '0' + str(next_day)
            else:
                str_day = str(next_day)
            next_date = str_year + str_month + str_day
            list_of_dates.append(next_date)

        for i in task.list_of_anti_tasks:
            if i.start_date in list_of_dates:
                list_of_dates.remove(i.start_date)
        return list_of_dates

    # returns True if name is a unique task name and False if not
    def check_task_name(self, name) -> bool:
        for i in self.list_of_tasks:
            if i.name == name:
                return False
        return True

    # returns True if date is valid and False if not
    def check_valid_date(self, date) -> bool:
        date = str(date)
        year = int(date[0:4])
        month = int(date[4:6])
        day = int(date[6:8])
        months_31 = [1, 3, 5, 7, 8, 10, 12]
        months_30 = [4, 6, 9, 11]

        if len(date) != 8:
            return False
        if day < 1:
            return False

        if month < 1 or month > 12:
            return False
        if month in months_31 and day > 31:
            return False
        elif month in months_30 and day > 30:
            return False
        elif month == 2:
            if year % 4 == 0 and day > 29:
                return False
            elif day > 28:
                return False

        return True
