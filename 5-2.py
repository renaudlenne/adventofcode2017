#!/usr/bin/python
import sys
from collections import Counter

if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print 'Syntax : %s <input>' % sys.argv[0]
        exit(1)

    filepath = sys.argv[1]
    nb_valid = 0
    with open(filepath) as fp:
        content = fp.readlines()
        content = [int(x.strip()) for x in content]
        nb_steps = 0
        i = 0
        while 0 <= i < len(content):
            nb_steps += 1
            prev_i = i
            i += content[prev_i]
            if content[prev_i] >= 3:
                content[prev_i] -= 1
            else:
                content[prev_i] += 1
        print nb_steps
