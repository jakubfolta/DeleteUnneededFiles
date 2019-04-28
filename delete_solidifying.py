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

# Create function for delete options.
def delete_option():
    answer = ''
    while answer not in ['yes', 'no']:
        print('Do you want to delete " {} " permanently?'.format(file))
        print('If "no", file will be send to trash from where you can restore it.')
        answer = input('Type "yes" or "no": ')
    if answer == 'yes':
        print('" {} " permanently deleted!\n'.format(file))
        #os.unlink(file_dir)
    elif answer == 'no':
        print('" {} " sent to trash. You can still restore it.\n'.format(file))
        #send2trash.send2trash(file_dir)

# Walk through given directory, check size of files and delete if needed.
for folder, subfolders, files in os.walk(dir_to_check):
    total_size = 0
    folder_basename = os.path.basename(folder)

    for file in files:
        file_size = os.path.getsize(os.path.join(folder, file))
        logging.info('File size: {}'.format(file_size))

        if file_size >= max_file_size:
            file_dir = os.path.join(folder, file)
            print('" {} " greater than 100MB'.format(file))
            delete_option()
            continue
        total_size += file_size
        logging.info('Total size is {}'.format(total_size))

    if total_size >= max_file_size and not subfolders:
        logging.info('Total size of " {} " is {}.'.format(folder_basename, total_size))
        answer = ''
        while answer not in ['yes', 'no']:
            print('Folder " {} " is greater than {}.'.format(folder_basename, max_file_size))
            print('Do you want to delete folder permanently? If "no", folder will be send to trash from where you can restore it.')
            answer = input('Type "yes" or "no": ')
        if answer == 'yes':
            print('" {} " permanently deleted!\n'.format(folder_basename))
            #os.unlink(folder)
        elif answer == 'no':
            print('" {} " sent to trash. You can still restore it.\n'.format(folder_basename))
            #send2trash.send2trash(folder)

    elif total_size >= max_file_size:
        print('Total size of files in " {} " is greater than {}. Files will be deleted.'.format(folder_basename, max_file_size))
        for file in files:
            file_dir = os.path.join(folder, file)
            delete_option()
else:
    print('Whole directory checked!')
