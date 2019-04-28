#! python3

'''del_unneeded_files.py - A program that walks through a folder tree and searches for exceptionally large files or folders.
Print these files with their absolute path to the screen.'''

# Import essential modules.
import os
import send2trash
import logging

logging.basicConfig(level = logging.DEBUG, format = '%(levelname)s, %(message)s')
logging.disable(logging.WARNING)

# Set directory to check and other variables.
dir_to_check = r'C:\Users\ogi-8\Desktop\PythonProjects\DelUnneededFiles\Sample_folder_to_check'
max_file_size = 104857600

logging.info('Max file size is {}.'.format(max_file_size))

# Walk through given directory, check size of files and delete if needed.
for folder, subfolders, files in os.walk(dir_to_check):
    total_size = 0
    folder_basename = os.path.basename(folder)

    for file in files:
        file_size = os.path.getsize(os.path.join(folder, file))
        logging.info('File size: {}'.format(file_size))
        if file_size >= max_file_size:
            file_dir = os.path.join(folder, file)
            print('{} is greater than {}. File deleted.'.format(file, max_file_size))
            #send2trash.send2trash(file_dir)
            continue
        total_size += file_size
        logging.info('Total size is {}'.format(total_size))
    if total_size >= max_file_size and not subfolders:
        logging.info('Total size of {} is {}.'.format(folder_basename, total_size))
        print('Folder {} is greater than {}. Folder deleted.'.format(folder_basename, max_file_size))
        #send2trash.send2trash(folder)
    elif total_size >= max_file_size:
        print('Total size of files in {} is greater than {}. Files will be deleted.'.format(os.path.basename(folder), max_file_size))
        for file in files:
            file_dir = os.path.join(folder, file)
            print('{} deleted.'.format(file))
            #send2trash.send2trash(file_dir)
else:
    print('Whole directory checked!')

def delete_option_():
    answer = ''
    while answer not in ['yes', 'no']:
        print('Do you want to delete files permanently? If no, files will be send to trash where you can restore them.')
        answer = input('Type "yes" or "no": ')
    if answer == 'yes':
        print('{} permanently deleted!'.format(file))
        #os.unlink(file_dir)
    elif answer == 'no':
        print('{} sent to trash. You can still restore it.'.format(file))
        #send2trash.send2trash(file_dir)
