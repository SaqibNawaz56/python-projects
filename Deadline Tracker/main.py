from calculating_remaining_days import cal_remaining_days
def main():
    try:
        with open('task.txt', 'r') as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        pass

    time_remaining, task, deadline = cal_remaining_days()
    days_left = time_remaining.days

    if days_left < 0:
        status = "Overdue"
    elif days_left == 0:
        status = "Due Today"
    elif 1 <= days_left <= 7:
        status = "Due this Week"
    else:
        status = "Future"

    print(f"Task: {task} | Status: {status}")

    with open("task.txt", 'a') as f:
        f.write(f"{task},{deadline}\n")

if __name__ == "__main__":
    main()