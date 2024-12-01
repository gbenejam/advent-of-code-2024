import sys
import os
from collections import Counter

# Add the parent directory to the path so we can import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

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

# Counting occurrences of each number in the columns
right_counts = Counter(right_column)

similarity = 0
# We calculate the similarity score by taking the number and multiplying it by the number of times it appears in the right column
for num in left_column:
    similarity += num * right_counts[num]

print(similarity)