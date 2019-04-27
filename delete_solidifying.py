#! python3

'''del_unneeded_files.py - A program that walks through a folder tree and searches for exceptionally large files or folders.
Print these files with their absolute path to the screen.'''

# Import essential modules.
import os
import send2trash
import logging

logging.basicConfig(level = logging.DEBUG, format = '%(levelname)s, %(message)s')

# Set directory to check and other variables.
dir_to_check = r'C:\Users\ogi-8\Desktop\PythonProjects\DelUnneededFiles\Sample_folder_to_check'
max_file_size = 104857600
total_size = 0

logging.info('Max file size is {}.'.format(max_file_size))
# TODO: Walk through given directory, check size of files and delete if needed.
for folder, subfolder, file in os.walk(dir_to_check):
    file_dir = os.path.join(folder, file)
    file_size = os.path.getsize(file)
    logging.info('File size: {}'.format(file_size))

    if file_size >= max_file_size:
        send2trash.send2trash(file_dir)
        continue
    total_size += file_size
    logging.info('Total size: {}'.format(total_size))

# TODO:
# TODO:
