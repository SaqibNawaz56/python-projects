def read_log_file(path):
    try:
        with open(path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def count_log_levels(lines):
    count = {
        "error_message": 0,
        "info_message": 0,
        "warning_message": 0
    }
    for line in lines:
        if 'ERROR' in line:
            count["error_message"] += 1
        elif 'INFO' in line:
            count["info_message"] += 1
        elif 'WARNING' in line:
            count["warning_message"] += 1

    return count

def count_logs_per_hour(lines):
    hour_count = {}

    for line in lines:
        hour = line[11:13]

        if hour in hour_count:
            hour_count[hour] += 1
        else:
            hour_count[hour] = 1

    return hour_count

def find_max_hour(hour_count):
    max_logs = 0
    max_hour = ""

    for h in hour_count:
        if hour_count[h] > max_logs:
            max_logs = hour_count[h]
            max_hour = h

    return max_hour, max_logs


def print_results(count, hour_count, max_hour, max_logs):
    print("ERROR:", count['error_message'])
    print("INFO:", count['info_message'])
    print("WARNING:", count['warning_message'])

    print("\nLogs per hour:")
    for h in hour_count:
        print(h + ":00 =", hour_count[h], "logs")

    print("\nMaximum logs:", max_logs, "at", max_hour + ":00")

def main():
    log_file_path = input("Please Enter the Path of File : ")

    lines = read_log_file(log_file_path)

    count = count_log_levels(lines)
    hour_count = count_logs_per_hour(lines)
    max_hour, max_logs = find_max_hour(hour_count)

    print_results(count, hour_count, max_hour, max_logs)

main()