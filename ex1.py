#!/usr/bin/python3

import glob
for files in glob.glob("*.py"):
    print(files)
    f = open('ex1.txt', 'a')
    f.writelines(files + "\n")
    f.close()