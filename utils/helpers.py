# Description: Helper functions for the project

# Function to read from a file, returns a String
def read_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()