import sys
import os

# Add the parent directory to the path so we can import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import utils.helpers as helpers

file_path = 'input.txt'
file_content = helpers.read_from_file(file_path)

# Convert file content to matrix
def parse_matrix(file_content):
    return [list(row) for row in file_content.strip().split('\n')]

possible_directions = [
    ((-1, -1), (1, 1)),  # Top-left to bottom-right diagonal
    ((-1, 1), (1, -1))   # Top-right to bottom-left diagonal
]

matrix = parse_matrix(file_content)
sum = 0

# Each position and its diagonals, center of the word is A (m-A-s or s-A-m)
for row in range(1, len(matrix) - 1): 
    for col in range(1, len(matrix[0]) - 1): 
        if matrix[row][col] == 'A': 
            valid_diagonal = True 
            for upper, lower in possible_directions:
                # Upper diagonal
                row1, col1 = row + upper[0], col + upper[1]
                # Lower diagonal
                row2, col2 = row + lower[0], col + lower[1]

                # Check if not out of bounds and form valid diagonal
                if not (0 <= row1 < len(matrix) and 0 <= col1 < len(matrix[0]) and
                        0 <= row2 < len(matrix) and 0 <= col2 < len(matrix[0])):
                    valid_diagonal = False
                    break

                if not (matrix[row1][col1] + matrix[row2][col2] in ['MS', 'SM']):
                    valid_diagonal = False
                    break

            # If both diagonals are valid, increment the sum
            if valid_diagonal:
                sum += 1

print(sum)
