def print_results(count, hour_count, max_hour, max_logs):
    print("Log Level Counts:")
    print("ERROR:", count.get('ERROR', 0))
    print("INFO:", count.get('INFO', 0))
    print("WARNING:", count.get('WARNING', 0))

    print("\nLogs per hour:")
    for h in sorted(hour_count.keys()):
        print(f"{h}:00 = {hour_count[h]} logs")

    print(f"\nMaximum logs: {max_logs} at {max_hour}:00")
