import os

path = 'test2.txt'

try:
    os.remove(path)
except FileNotFoundError:
    print('That file was not found')