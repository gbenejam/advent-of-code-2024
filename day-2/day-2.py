import sys
import os

# Add the parent directory to the path so we can import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.helpers as helpers

file_path = 'input.txt'
file_content = helpers.read_from_file(file_path)

def split_lines(file_content):
    lines = []
    for line in file_content.split('\n'):
        if line.strip():
            array = [int(x) for x in line.split()]
            lines.append(array)
    return lines

reports = split_lines(file_content)

# is ascending or descending
def is_sorted(report):
    return all((report[i] <= report[i + 1] and 1 <= abs(report[i + 1] - report[i]) <= 3 ) for i in range(len(report) - 1)) or \
              all((report[i] >= report[i + 1] and 1 <= abs(report[i + 1] - report[i]) <= 3) for i in range(len(report) - 1))

sum_safe = 0
# Checking if safe or not
for report in reports:
    if is_sorted(report):
        sum_safe += 1

print(sum_safe)