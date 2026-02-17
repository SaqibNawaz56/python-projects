def count_specific_message():

    log_file_path = 'C:/python-projects/log.txt'

    count = {
        "error_message": 0,
        "info_message": 0,
        "warning_message": 0
    }

    hour_count = {}

    try:
        with open(log_file_path, 'r') as file:
            for line in file:

                if 'ERROR' in line:
                    count["error_message"] += 1
                elif 'INFO' in line:
                    count["info_message"] += 1
                elif 'WARNING' in line:
                    count["warning_message"] += 1

                hour = line[11:13]

                if hour in hour_count:
                    hour_count[hour] += 1
                else:
                    hour_count[hour] = 1

    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    max_logs = 0
    max_hour = ""

    for h in hour_count:
        if hour_count[h] > max_logs:
            max_logs = hour_count[h]
            max_hour = h

    print("ERROR:", count['error_message'])
    print("INFO:", count['info_message'])
    print("WARNING:", count['warning_message'])

    print("\nLogs per hour:")
    for h in hour_count:
        print(h + ":00 =", hour_count[h], "logs")

    print("\nMaximum logs:", max_logs, "at", max_hour + ":00")


count_specific_message()
