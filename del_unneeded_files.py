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
    subfolder_exist = 0
    for x in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, x)):
            subfolder_exists = 1
            break
    for file in files:
        print(subfolder_exists)
    #     file_abspath = os.path.join(folder, file)
    #     file_size = os.path.getsize(file_abspath)
    #     if file_size >= file_size_to_del:
    #         print('File size greater than 100MB. Size: {}\nFile:\n{}\nSend to trash.'.format(file_size, file_abspath))
    #         #send2trash.send2trash(file_abspath)
    #         continue
    #     total_size = total_size + file_size
    # if total_size >= file_size_to_del and folder != dir_to_check: #and subfolder_exists == False:
    #     print('Size of files greter than 100MB. Size: {}\nFolder:\n{}\nSend to trash.'.format(total_size, folder))
    #     #send2trash.send2trash(folder)


# TODO:
