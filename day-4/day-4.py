import sys
import os
import re

# Add the parent directory to the path so we can import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.helpers as helpers

file_path = 'input.txt'
file_content = helpers.read_from_file(file_path)
possible_directions = [
    (0,1),
    (1,0),
    (0,-1),
    (-1,0),
    (1,1),
    (-1,-1),
    (-1,1),
    (1,-1)
]
sum_of_directions = 0
word = 'XMAS'

# Converting file content to matrix
matrix = [list(row) for row in file_content.strip().split('\n')]

# Checking each position in the matrix and checking every direction to see if there's XMAS
for column in range(len(matrix)):
    for row in range(len(matrix[0])):
        for x,y in possible_directions:
            rows = len(matrix)
            columns = len(matrix[0])
            word_length = len(word)
            found = True

            for i in range(word_length):
                # Calculate the next position for the word
                new_column, new_row = column + i * x, row + i * y
                # Checking if out of bounds and if the characters matches the word
                if not (0 <= new_column < rows and 0 <= new_row < columns) or (matrix[new_column][new_row] != word[i]):
                    found = False
                    break

            if found:
                sum_of_directions += 1

print(sum_of_directions)


