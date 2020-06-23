import os
import sys
import fileinput


for line in fileinput.input("python/test/test.txt", inplace=True):
    line = line.replace("t = True", "t = False")
    sys.stdout.write(line)
