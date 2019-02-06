#!/usr/bin/env python
import os
from datetime import datetime

FOLDER = 'DATA'
FILE_NAME = 'mary.txt'

file_path = os.path.join(FOLDER, FILE_NAME)

print("path:", file_path)
file_size = os.path.getsize(file_path)
print("size:", file_size)
raw_timestamp = os.path.getmtime(file_path)
print("raw timestamp:", raw_timestamp)

print("abs path:", os.path.abspath(file_path))

print('dir:', os.path.dirname(file_path))
print("base:", os.path.basename(file_path))

print('is dir?', os.path.isdir(file_path))
print('is file?', os.path.isfile(file_path))
print('exists?', os.path.exists(file_path))

print("Can read?", os.access(file_path, os.R_OK))
print("Can write?", os.access(file_path, os.W_OK))

print(os.stat(file_path))

print("split:", os.path.split(file_path))

print("split:", os.path.split(os.path.abspath(file_path)))
print('-' * 60)
for file_name in os.listdir('DATA'):
    print(file_name)
print()

print('-' * 60)
for file_obj in os.scandir('DATA'):
    print(file_obj.name)
print()

# start_dir = os.path.abspath('.')
start_dir = '.'

for currdir, dir_list, file_list in os.walk(start_dir):
    if 'git' in currdir:
        continue
    print(currdir)
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(currdir, file_name)
            file_size = os.path.getsize(file_path)
            file_raw_ts = os.path.getmtime(file_path)
            file_ts = datetime.fromtimestamp(file_raw_ts).date()
            print(f"  {file_size:8d} {file_ts} {file_name}")
