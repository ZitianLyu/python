import os
import shutil
from util import strip_path

def create_file(file_name):
    file_name = strip_path(file_name)
    is_exists = os.path.exists(file_name)
    if not is_exists:
        with open(file_name, mode='wb') as file:
            file.write(bytes('hello binary', 'ascii'))
            file.close()
        print(file_name + ' was created successful.')
        return True
    else:
        print(file_name + ' file already exists.')
        return False

def read_file(file_name):
    file_name = strip_path(file_name)
    is_exists = os.path.exists(file_name)
    if not is_exists:
        print('Can\'t find ' + file_name)
        return
    with open(file_name, 'rb') as file:
        file_content = file.read()
        file.close()
    return file_content

def move_file(old_file_name, new_file_name):
    old_file_name = strip_path(old_file_name)
    is_exists = os.path.exists(old_file_name)
    if not is_exists:
        print('The name “' + old_file_name + '” is already taken. Please choose a different name.')
        return False
    else:
        shutil.move(old_file_name, new_file_name)
    return True

def delete_file(file_name):
    file_name = strip_path(file_name)
    is_exists = os.path.exists(file_name)
    if not is_exists:
        print('Can\'t find ' + file_name)
        return False
    else:
        os.remove(file_name)
    return True


