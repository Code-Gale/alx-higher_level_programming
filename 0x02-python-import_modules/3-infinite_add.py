#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    add = 0
    for inf in argv[1:]:
        add += int(inf)
    print("{:d}".format(add))
