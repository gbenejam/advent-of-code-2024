import sys
import os
import re

# Add the parent directory to the path so we can import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import utils.helpers as helpers

file_path = 'input.txt'
file_content = helpers.read_from_file(file_path)
# Updated pattern to include do() and don't()
regex_pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)";
sum = 0
compute = True

def parse_input(file_content):
    return re.findall(regex_pattern, file_content)

instructions = parse_input(file_content)

# If we have do, we take into account the next muls. If don't, we ignore them.
for instruction in instructions:
    if instruction == 'do()':
        compute = True
    elif instruction == "don't()":
        compute = False
    elif "mul(" in instruction and compute:
        find = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", instruction)
        if find:  
            a, b = find[0] 
            sum += int(a) * int(b)

print(sum)

