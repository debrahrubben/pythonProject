import os

path='C:\\Users\\Cyrus\\Desktop\\Android'
if os.path.exists(path):
    print('That location exist')
    if os.path.isfile(path):
        print('it is a file')
    elif os.path.isdir(path):
        print('it is a directory')
else:
    print('that location does not exist')