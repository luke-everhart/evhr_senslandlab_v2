# Usage: parse_file_struct.py [/path/to/root/] [/path/to/output]

from sys import argv
import os

path = argv[1]

imagery_files = []

for (root, dirs, file) in os.walk(path):
    for f in file:
        if ".ntf" in f:
            imagery_files.append(os.path.join(root, f))


with open(argv[2], 'w') as f:
    for line in imagery_files:
        f.write(line)
        f.write('\n')
