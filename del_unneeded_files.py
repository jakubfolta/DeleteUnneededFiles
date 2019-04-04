#! python3

'''del_unneeded_files.py - A program that walks through a folder tree and searches for exceptionally large files or folders.
Print these files with their absolute path to the screen.'''

# Import essential modules.
import os
import send2trash

# Set directory to check and file size to delete.
dir_to_check = r'C:\Users\ogi-8\Desktop\PythonProjects\DelUnneededFiles\Sample_folder_to_check'
file_size_to_del = 104857600

# Walk through folder tree and delete big files.
for folder, subfolders, files in os.walk(dir_to_check):
    total_size = 0
    for file in files:
        file_abspath = os.path.join(folder, file)
        file_size = os.path.getsize(file_abspath)
        if file_size >= file_size_to_del:
            folder_basename = os.path.basename(folder)
            print('Size of "{}" file greater than 100 MB.'.format(file))
            print('Size of file: {}'.format(file_size))
            print(File: "{}" in folder "{}" send to trash..format(file, folder_basename))
            #send2trash.send2trash(file_abspath)
            continue
        total_size = total_size + file_size                     # Delete folder if current folder doesn't contain any subfolders
    if total_size >= file_size_to_del and not subfolders:       # and size is bigger than 100 MB
        print('Size of files in "{}" folder greter than 100MB.'.format(folder_basename))
        print('Size of folder: "{}"'.format(total_size))
        print('Folder: "{}" send to trash'.format(folder_basename))
        #send2trash.send2trash(folder)
else:
    print('Directory checked and big files deleted.')
