#!/usr/bin/python3
import sys

# Command Line args
try:
    original_fileName = sys.argv[1]
    new_fileName = sys.argv[2]
except IndexError:
    print('There must be 2 arguments')
    sys.exit()

# Open Each File
originalFile = open(original_fileName, "r")
newFile = open(new_fileName, "r")
# Read Each Line by Line and get rid of the new lines
with originalFile as f:
    file1 = f.read().splitlines()
with newFile as f2:
    file2 = f2.read().splitlines()

# Check each element and see if they don't match
for i in range(len(file1)):
    if file1[i] != file2[i]:
        exe = file1[i].split()[0]
        print(exe + ': MD5 original = ' + file1[i] + ', MD5 new = ' + file2[i])

# Close files
originalFile.close()
newFile.close()
