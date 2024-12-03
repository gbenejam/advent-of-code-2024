import sys
import os
import re

# Add the parent directory to the path so we can import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.helpers as helpers

file_path = 'input.txt'
file_content = helpers.read_from_file(file_path)
regex_pattern = r"mul\((\d{1,3}),(\d{1,3})\)";
sum = 0

def parse_input(file_content):
    return re.findall(regex_pattern, file_content)

# integers instead of strings
pairs_int = [(int(a), int(b)) for a,b in parse_input(file_content)]
for pair in pairs_int:
    sum += pair[0] * pair[1]

print(sum)
