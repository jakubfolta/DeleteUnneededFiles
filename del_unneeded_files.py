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
    #print(folder)
    if subfolders:
        print('y')
    # for x in os.listdir(folder):
    #     if os.path.isdir(os.path.join(folder, x)):
    #         subfolder_exists = 1
    #         break
    for file in files:
        file_abspath = os.path.join(folder, file)
        file_size = os.path.getsize(file_abspath)
        if file_size >= file_size_to_del:
            print('File size greater than 100MB.\nSize of file: {}\n\nFile: "{}" in folder "{}" send to trash.'.format(file_size, file, os.path.basename(folder)))
            #send2trash.send2trash(file_abspath)
            continue
        total_size = total_size + file_size
    if total_size >= file_size_to_del and folder != dir_to_check and not subfolders:
        print('Size of files greter than 100MB. \nSize of folder: {}\n\nFolder: "{}" send to trash.'.format(total_size, os.path.basename(folder)))
        #send2trash.send2trash(folder)


# TODO:
