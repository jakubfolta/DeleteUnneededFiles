#! python3

# del_unn_files.py - A program that walks through a folder tree and searches for exceptionally large files or folders.
# Print these files with their absolute path to the screen.

# Import essential modules.
import os
import send2trash

# Set the directory to check.
dir_to_check = r'C:\Users\ogi-8\Desktop\PythonProjects\DelUnneededFiles\Sample_folder_to_check'

# Write function to print absolute path to files (100 MB and more file size).
def search_print_big_files(x):
    if os.path.getsize(x) >= 104857600:
        print('Direction greater than 100 MB: {}'.format(x))

# Walk selected directory with os.walk()
for folder, subfolders, files in os.walk(dir_to_check):
    abs_path = folder
    search_print_big_files(abs_path)
    #print(abs_path)
    for file in files:
        abs_path = os.path.join(folder, file)
        search_print_big_files(abs_path)
        #print(abs_path)
# TODO: Change project status on github.
