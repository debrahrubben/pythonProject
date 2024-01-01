import os.path

source = 'copy.txt'
destination = 'C:\\Users\\Cyrus\\Desktop\\moved.txt'

try:
    if os.path.exists(destination):
        print('there is a file there already')
    else:
        os.replace(source,destination)
        print(source+' was moved')
except FileNotFoundError:
    print(source+' was not found')