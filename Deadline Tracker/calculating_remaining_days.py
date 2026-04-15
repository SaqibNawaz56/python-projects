import datetime as datetime
def cal_remaining_days():
    task = input("Please Enter the Task: ")
    year = int(input("Enter Year (e.g. 2026): "))
    month = int(input("Enter Month (1-12): "))
    day = int(input("Enter Day (1-31): "))
    deadline = datetime.datetime(year, month, day)
    print(f"Task: {task}")
    print(f"Deadline: {deadline}")
    time_remaining = deadline-datetime.datetime.now()
    return  time_remaining,task,deadline