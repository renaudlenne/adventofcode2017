#!/usr/bin/python
import sys
import re
from collections import defaultdict


if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print('Syntax : %s <input>' % sys.argv[0])
        exit(1)

    filepath = sys.argv[1]
    with open(filepath) as fp:
        instructions = [int(x.strip()) for x in fp.readlines()[0].split(',')]
        circle = list(range(256))
        position = 0
        skip = 0
        for instruction in instructions:
            if position+instruction <= len(circle):
                circle[position:position+instruction] = reversed(circle[position:position+instruction])
            else:
                nb_at_start = position+instruction-len(circle)
                nb_at_end = instruction-nb_at_start
                reversed_chunk = list(reversed(circle[-nb_at_end:] + circle[:nb_at_start]))
                circle[-nb_at_end:] = reversed_chunk[:nb_at_end]
                circle[:nb_at_start] = reversed_chunk[-nb_at_start:]
            position = (position + instruction + skip) % len(circle)
            skip += 1
    print(circle[0]*circle[1])
