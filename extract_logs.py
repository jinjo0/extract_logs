import os
import re

# Get the current directory
current_directory = os.getcwd()

# Define a regular expression pattern to match links containing "bybit.com"
pattern = re.compile(r'\b(?:https?://)?(?:www\.)?bybit\.com\S+\b')

# List all .txt files in the current directory
txt_files = [file for file in os.listdir(current_directory) if file.endswith('.txt')]

# Iterate through each .txt file
for txt_file in txt_files:
    with open(txt_file, 'r') as file:
        # Read the contents of the file
        file_content = file.read()
        
        # Find all matches of the pattern in the file content
        matches = pattern.findall(file_content)
        
        # If matches are found, write them to a file named 'bybit.notxt'
        if matches:
            with open('bybit.notxt', 'a') as bybit_file:
                bybit_file.write(f"Links in {txt_file}:\n")
                for match in matches:
                    bybit_file.write(match + '\n')
                bybit_file.write('\n')
