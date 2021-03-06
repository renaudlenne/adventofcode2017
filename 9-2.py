#!/usr/bin/python
import sys
import re
from collections import defaultdict


def parse_content(content):
    stack = []
    in_garbage = False
    ignore_char = False
    freed_garbage = 0
    for i, c in enumerate(content):
        if ignore_char:
            ignore_char = False
            continue
        if in_garbage:
            if c == '!':
                ignore_char = True
            elif c == '>':
                in_garbage = False
            else:
                freed_garbage += 1
        else:
            if c == '<':
                in_garbage = True
            elif c == '{':
                stack.append(i)
            elif c == '}' and stack:
                stack.pop()
    return freed_garbage

if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print('Syntax : %s <input>' % sys.argv[0])
        exit(1)

    filepath = sys.argv[1]
    with open(filepath) as fp:
        result = parse_content(fp.readlines()[0])
    print(result)
