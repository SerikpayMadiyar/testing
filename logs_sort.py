import re
from datetime import datetime

# Example log lines
logs = [
    "[2023-05-10 10:30:01] Error: Database failure",
    "[2023-05-10 09:15:45] Info: System start",
    "[2023-05-10 10:05:12] Warning: High memory usage"
]

def get_timestamp(line):
    # Adjust regex to match your log's date format
    match = re.search(r'\[(.*?)\]', line)
    if match:
        return datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
    return datetime.min

# Sort logs based on the extracted timestamp
sorted_logs = sorted(logs, key=get_timestamp)

for log in sorted_logs:
    print(log)
