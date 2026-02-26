import re
from collections import Counter

def count_log_levels(lines):
    log_level = re.compile(r'\b(INFO|WARNING|ERROR)\b', re.IGNORECASE)
    count = Counter()
    for line in lines:
        match = log_level.search(line)
        if match:
            level = match.group(1).upper()
            count[level] += 1
    return dict(count)
