#! python3

'''del_unneeded_files.py - A program that walks through a folder tree and searches for exceptionally large files or folders.
Print these files with their absolute path to the screen.'''

# Import essential modules.
import os
import send2trash

# Set directory to check and file size to delete.
dir_to_check = r'C:\Users\ogi-8\Desktop\PythonProjects\DelUnneededFiles\Sample_folder_to_check'
file_size = 104857600

# TODO: Walk through folder tree and search for big files.
for folder, subfolders, files in os.walk(dir_to_check):
    total_size = 0
    for file in files:
        if os.path.getsize(file) >= file_size:
            print()
            #send2trash.send2trash


# TODO:
