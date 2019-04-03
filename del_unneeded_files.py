#! python3

'''del_unneeded_files.py - A program that walks through a folder tree and searches for exceptionally large files or folders.
Print these files with their absolute path to the screen.'''

# Import essential modules.
import os
import send2trash

# Set directory to check and file size to delete.
dir_to_check = r'C:\Users\ogi-8\Desktop\PythonProjects\DelUnneededFiles\Sample_folder_to_check'
file_size_to_del = 104857600

# TODO: Walk through folder tree and search for big files.
for folder, subfolders, files in os.walk(dir_to_check):
    total_size = 0
    for file in files:
        file_size = os.path.getsize(file)
        if file_size >= file_size_to_del:
            file_abspath = os.path.join(folder, file)
            print('File size greater than 100MB. Size: {}\nFile:\n{}\nSend to trash.'.format(file_size, file_abspath))
            #send2trash.send2trash(file_abspath)
            continue
        total_size = total_size + file_size
        



# TODO:
