import sys
import os

# Add the parent directory to the path so we can import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.helpers as helpers

file_path = 'input.txt'
file_content = helpers.read_from_file(file_path)

# Separating the numbers in left and right column
def split_left_right_columns(file_content):
    left = []
    right = []
    for line in file_content.split('\n'):
        if line.strip():
            parts = line.split()
            left.append(int(parts[0]))
            right.append(int(parts[1]))
    return left, right

left_column = split_left_right_columns(file_content)[0]
right_column = split_left_right_columns(file_content)[1]

# Now we need to apply quicksort to sort columns from smaller to bigger
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

sorted_left_column = quicksort(left_column)
sorted_right_column = quicksort(right_column)

all_pairs = []
# Now we substract the paired numbers
for pair in zip(sorted_left_column, sorted_right_column):
    all_pairs.append(abs(pair[1] - pair[0]))

# Now we sum all the differences
result = sum(all_pairs)
print(result)