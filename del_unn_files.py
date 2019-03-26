#! python3

# del_unn_files.py - A program that walks through a folder tree and searches for exceptionally large files or folders.
# Print these files with their absolute path to the screen.

# Import essential modules.
import os
import send2trash

# Set the directory to check.
dir_to_check = r'C:\Users\ogi-8\Desktop\PythonProjects\DelUnneededFiles\Sample folder to check'

# Write function to print absolute path to files (100 MB and more file size).
def search_print_big_files(x):
    if os.path.getsize(x) >= 104857600:
        print('Direction greater than 100 MB: {}'.format(abs_path))

# TODO: Walk selected directory with os.walk()
for folder, subfolder, file in os.walk(dir_to_check):
        


# TODO: Change project status on github.
