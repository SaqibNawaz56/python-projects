from printing_results import print_results
from hourly_logs import count_logs_per_hour, find_max_hour
from counting_log import  count_log_levels
from reading_logs import read_logs_file


def main():
    log_file_path = input("Please Enter the Path of File: ")
    lines = read_logs_file(log_file_path)

    if not lines:
        return

    count = count_log_levels(lines)
    hour_count = count_logs_per_hour(lines)
    max_hour, max_logs = find_max_hour(hour_count)

    print_results(count, hour_count, max_hour, max_logs)


if __name__ == "__main__":
    main()
