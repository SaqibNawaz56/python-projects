import re
from collections import Counter
from datetime import datetime

def count_logs_per_hour(lines):
    hour_count = Counter()
    hours_reg = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    time_pattern = '%Y-%m-%d %H:%M:%S'

    for line in lines:
        match = hours_reg.search(line)
        if match:
            timestamp_str = match.group()
            timestamp = datetime.strptime(timestamp_str, time_pattern)
            hour = timestamp.hour
            hour_count[hour] += 1

    return dict(hour_count)


def find_max_hour(hour_count):
    max_logs = 0
    max_hour = None
    for h in hour_count:
        if hour_count[h] > max_logs:
            max_logs = hour_count[h]
            max_hour = h
    return max_hour, max_logs
