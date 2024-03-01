import os

# Function to search for kuna.io in a line and save it to kuna.io.txt
def search_and_save(filename,domain):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            if domain in line:
                file_name = domain+".txt"
                with open(file_name, 'a', encoding='utf-8') as output_file:
                    output_file.write(line)

# List all files in the current directory
files = os.listdir()
domain="advcash.com"
# Iterate over each file and search for kuna.io
for file in files:
    if os.path.isfile(file):  # Check if it's a file
        search_and_save(file,domain)
