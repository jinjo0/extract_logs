import os

# Get the current directory
current_directory = os.getcwd()

# List all .txt files in the current directory
txt_files = [file for file in os.listdir(current_directory) if file.endswith('.txt')]

# Iterate through each .txt file
for txt_file in txt_files:
    with open(txt_file, 'r', encoding='utf-8') as file:
        # Read the contents of the file line by line
        lines = file.readlines()
        
        # Open the output file for appending
        with open('bybit.notxt', 'a', encoding='utf-8') as bybit_file:
            # Iterate through each line in the file
            for line in lines:
                # Search for the presence of "bybit" in the line
                if "bybit" in line:
                    # If found, write the line to the output file
                    bybit_file.write(line)
