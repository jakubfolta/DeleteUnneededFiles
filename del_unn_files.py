#! python3

# del_unn_files.py - A program that walks through a folder tree and searches for exceptionally large files or folders.
# Print these files with their absolute path to the screen.

# Import essential modules.
import os
import send2trash

# Set the directory to check.
dir_to_check = r'C:\Users\ogi-8\Desktop\PythonProjects\DelUnneededFiles\Sample_folder_to_check'

# Walk selected directory with os.walk()
for folder, subfolders, files in os.walk(dir_to_check):
    files_total_size = 0
    #print(abs_path)
    #print(abs_path)
    for file in files:
        file_abs_path = os.path.join(folder, file)
        file_size = os.path.getsize(file_abs_path)
        if file_size >= 104857600:
            print('File bigger than 100 MB:\n{}\nSize: {}\nDeleted.'.format(file_abs_path, file_size))
            #send2trash.send2trash(file_abs_path)
        files_total_size = files_total_size + os.path.getsize(file_abs_path)
    if files_total_size >= 104857600:
        print('Folder size bigger than 100 MB:\n{}\nDeleted.'.format(folder))
    print(files_total_size)
        #print(abs_path)
# TODO: Change project status on github.
